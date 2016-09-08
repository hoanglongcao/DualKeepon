/* 
 * Written for the HRI Summer School 2013 - http://www.hrisummerschool.org/
 * 
 * A joint effort between:
 * VUB Robotics and MultiBody Mechanics Research Group - http://mech.vub.ac.be/multibody_mechanics.htm
 * and
 * Plymouth University Centre for Robotics and Neural Systems - https://www1.plymouth.ac.uk/research/crns/Pages/default.aspx
 * 
 * 
 * Project:    ViKeepon
 * Author:     CAO Hoang Long
 * Created:    Feb 2012
 * Contact:    http://chlong.tk or http://vikeepon.tk
 * 
 * Modified by James Kennedy to work with MyKeepon framework by BeatBots - Aug 2013
 *  https://github.com/BeatBots/MyKeepon
 *  http://www.tech.plym.ac.uk/SoCCE/CRNS/staff/JKennedy/
 * 
 * Tested using a MyKeepon model KP1001 at 115200 Baud, default TWI from BeatBots set in Arduino code
 * 
 */

#region Namespace Inclusions
using System;
    using System.Data;
    using System.Text;
    using System.Drawing;
    using System.IO.Ports;
    using System.Windows.Forms;
    using System.ComponentModel;
    using System.Collections.Generic;
    using SerialPortTerminal.Properties;
    using System.Media;
    using System.Threading;
    using System.IO;
    using System.Diagnostics;
#endregion

namespace SerialPortTerminal
{
  #region Public Enumerations
    public enum DataMode1 { Text, Hex }
    public enum LogMsgType1 { Incoming, Outgoing, Normal, Warning, Error };
  #endregion

  public partial class frmTerminal1 : Form
  {
    #region Local Variables
      private SerialPort comport = new SerialPort();    // The main control for communicating through the RS-232 port
      private Color[] LogMsgTypeColor = { Color.Blue, Color.Green, Color.Black, Color.Orange, Color.Red };    // Various colors for logging info
      private bool KeyHandled = false;                  // Temp holder for whether a key was pressed
    #endregion

    #region Constructor
        public frmTerminal1()
        {
            InitializeComponent();      // Build the form
            InitializeControlValues();  // Restore the users settings
            EnableControls();           // Enable/disable controls based on the current state
            comport.DataReceived += new SerialDataReceivedEventHandler(port_DataReceived);  //add com port event handler
        }
    #endregion

    #region Creator/Affiliation Links
        private void lblJKSite_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            ProcessStartInfo sInfo = new ProcessStartInfo("http://www.tech.plym.ac.uk/SoCCE/CRNS/staff/JKennedy/");
            Process.Start(sInfo);
        }

        private void lblViKeepon_Click(object sender, EventArgs e)
        {
            ProcessStartInfo sInfo = new ProcessStartInfo("http://probo.vub.ac.be/HackingKeepon");
            Process.Start(sInfo);
        }

        private void picVUB_Click(object sender, EventArgs e)
        {
            ProcessStartInfo sInfo = new ProcessStartInfo("http://mech.vub.ac.be/multibody_mechanics.htm");
            Process.Start(sInfo);
        }

        private void picPlym_Click(object sender, EventArgs e)
        {
            ProcessStartInfo sInfo = new ProcessStartInfo("https://www1.plymouth.ac.uk/research/crns/Pages/default.aspx");
            Process.Start(sInfo);
        }

        private void lnkSumSch_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            ProcessStartInfo sInfo = new ProcessStartInfo("http://www.hrisummerschool.org/");
            Process.Start(sInfo);
        }
    #endregion

    #region Local Methods
        /// <summary> Save the user's settings. </summary>
        private void SaveSettings()
        {
            Settings.Default.BaudRate = int.Parse(cmbBaudRate.Text);
            Settings.Default.DataBits = int.Parse(cmbDataBits.Text);
            Settings.Default.Parity = (Parity)Enum.Parse(typeof(Parity), cmbParity.Text);
            Settings.Default.StopBits = (StopBits)Enum.Parse(typeof(StopBits), cmbStopBits.Text);
            Settings.Default.PortName = cmbPortName.Text;
            Settings.Default.Save();
        }

        /// <summary> Populate the form's controls with default settings. </summary>
        private void InitializeControlValues()
        {
          cmbParity.Items.Clear(); cmbParity.Items.AddRange(Enum.GetNames(typeof(Parity)));
          cmbStopBits.Items.Clear(); cmbStopBits.Items.AddRange(Enum.GetNames(typeof(StopBits)));

          cmbParity.Text = Settings.Default.Parity.ToString();
          cmbStopBits.Text = Settings.Default.StopBits.ToString();
          cmbDataBits.Text = Settings.Default.DataBits.ToString();
          cmbParity.Text = Settings.Default.Parity.ToString();
          cmbBaudRate.Text = Settings.Default.BaudRate.ToString();
         
          cmbPortName.Items.Clear();
          foreach (string s in SerialPort.GetPortNames())
            cmbPortName.Items.Add(s);

          if (cmbPortName.Items.Contains(Settings.Default.PortName)) cmbPortName.Text = Settings.Default.PortName;
          else if (cmbPortName.Items.Count > 0) cmbPortName.SelectedIndex = 0;
          else
          {
            MessageBox.Show(this, "There are no COM Ports detected on this computer.\nPlease install a COM Port and restart this app.", "No COM Ports Installed", MessageBoxButtons.OK, MessageBoxIcon.Error);
            this.Close();
          }
        }

        /// <summary> Enable/disable controls based on the app's current state. </summary>
        private void EnableControls()
        {
          // Enable/disable controls based on whether the port is open or not
          gbPortSettings.Enabled = !comport.IsOpen;
          txtSendData.Enabled = btnSend.Enabled = comport.IsOpen;
      
          groupBox_Sounds.Enabled = comport.IsOpen;
          groupBox_Movements.Enabled = comport.IsOpen;

         

          if (comport.IsOpen) { btnOpenPort.Text = "&Close Port";}
          else { btnOpenPort.Text = "&Open Port";}
        }

        /// <summary> Send the user's data currently entered in the 'send' box.</summary>
        private void SendData(string sData)
        {
            sendString(sData, "User command"); 
            txtSendData.SelectAll();
        }
    
        /// <summary> Log data to the terminal window. </summary>
        /// <param name="msgtype"> The type of message to be written. </param>
        /// <param name="msg"> The string containing the message to be shown. </param>
        private void Log(LogMsgType msgtype, string msg)
        {
          rtfTerminal.Invoke(new EventHandler(delegate
          {
            rtfTerminal.SelectedText = string.Empty;
            rtfTerminal.SelectionFont = new Font(rtfTerminal.SelectionFont, FontStyle.Bold);
            rtfTerminal.SelectionColor = LogMsgTypeColor[(int)msgtype];
            rtfTerminal.AppendText(msg);
            rtfTerminal.ScrollToCaret();
          }));
        }
    #endregion

    #region Event Handlers
        private void frmTerminal_Shown(object sender, EventArgs e)
        {
          Log(LogMsgType.Error, String.Format("Welcome to ViKeepon!\n"));
        }

        private void btnOpenPort_Click(object sender, EventArgs e)
        {
            // If the port is open, close it.
            if (comport.IsOpen)
            {
                try
                {
                    comport.Close();
                    Log(LogMsgType.Warning, String.Format(cmbPortName.Text + " is closed!\n"));
                }
                catch (IOException)
                {
                    Log(LogMsgType.Error, String.Format(cmbPortName.Text + " is not connected. Try again!\n"));
                }
            }
            else
            {
                // Set the port's settings
                comport.BaudRate = int.Parse(cmbBaudRate.Text);
                comport.DataBits = int.Parse(cmbDataBits.Text);
                comport.StopBits = (StopBits)Enum.Parse(typeof(StopBits), cmbStopBits.Text);
                comport.Parity = (Parity)Enum.Parse(typeof(Parity), cmbParity.Text);
                comport.PortName = cmbPortName.Text;

                // Open the port
                try
                {
                    comport.Open();
                }
                catch (IOException)
                {
                    Log(LogMsgType.Error, String.Format(cmbPortName.Text + " is not connected. Try again!\n"));
                }
                catch (UnauthorizedAccessException)
                {
                    Log(LogMsgType.Error, String.Format(cmbPortName.Text + " is in used!\n"));
                }
            }

            // Change the state of the form's controls
            EnableControls();

            // If the port is open, send focus to the send data box
            if (comport.IsOpen)
            {
                txtSendData.Focus();
                Log(LogMsgType.Outgoing, String.Format(cmbPortName.Text + " is ready!\n"));
            }
        }

        private void frmTerminal_FormClosing(object sender, FormClosingEventArgs e) { SaveSettings(); }
        private void cmbBaudRate_Validating(object sender, CancelEventArgs e) { int x; e.Cancel = !int.TryParse(cmbBaudRate.Text, out x); }
        private void cmbDataBits_Validating(object sender, CancelEventArgs e) { int x; e.Cancel = !int.TryParse(cmbDataBits.Text, out x); }
        private void txtSendData_KeyDown(object sender, KeyEventArgs e) { if (KeyHandled = e.KeyCode == Keys.Enter) { e.Handled = true; SendData(txtSendData.Text); } }
        private void txtSendData_KeyPress(object sender, KeyPressEventArgs e) { e.Handled = KeyHandled; }
        private void btnSend_Click(object sender, EventArgs e) { SendData(txtSendData.Text); }
        private bool checkbitclear(byte b, int pos) { return (~b & (1 << pos)) != 0; }  

       private void port_DataReceived(object sender, SerialDataReceivedEventArgs e)
       {
            try
            {
                //important to use readline not readexisting, as then we wait for complete string returns (use serial.println in arduino code)
                string sReceived = comport.ReadLine(); 

                //uncomment line below to stop seeing the incessant audio update messages in terminal
                //if ((!sReceived.Contains("AUDIO")) && ((!sReceived.Contains("RANGE")) || (!sReceived.Contains("MEAN"))))
                    Log(LogMsgType.Incoming, sReceived + "\n");

                ReceivedListener(sReceived);    //go to our event listener to implement behaviours
            }
            catch { }
       }

       private void ReceivedListener(string sInput)
       {
           //ADD HERE CODE TO MODIFY MOTION AND SOUNDS OF BUTTON TOP OF HEAD

           /*
            * watch for events here and call functions, e.g.:
            * 
            * if (sInput.Contains("BUTTON HEAD ON"))
            * {
            *       sendString("SOUND PLAY 12;", "Head touched");
            * }
            * 
            */
       }
    #endregion

    #region KEEPON COMMANDS - useful for reference
    /*
     * Allowable commands (the closing semicolon is required):
        SOUND PLAY <0...63>;
        SOUND REPEAT <0...63>;
        SOUND DELAY <msec>;
        SOUND STOP;
        SPEED [PAN, TILT, PONSIDE] <0...255>;
        MOVE PAN <-100...100>;
        MOVE TILT <-100...100>;
        MOVE SIDE [CYCLE, CENTERFROMLEFT, RIGHT, CENTERFROMRIGHT, LEFT];
        MOVE PON [UP, HALFDOWN, DOWN, HALFUP];
        MOVE STOP;
        MODE [DANCE, TOUCH];
        MODE TEMPO;
        MODE SLEEP;

        Strings that the Arduino can send back to you:
        BUTTON [DANCE, TOUCH] [OFF, ON]
        BUTTON [HEAD, FRONT, BACK, RIGHT, LEFT] [OFF, ON]
        MOTOR [PAN, TILT, SIDE, PON] FINISHED
        MOTOR [PAN, TILT, SIDE, PON] STALLED
        ENCODER TILT [NOREACH, FORWARD, BACK, UP]
        ENCODER PON [HALFDOWN, UP, DOWN, HALFUP]
        ENCODER SIDE [CENTER, RIGHT, LEFT]
        ENCODER PAN [BACK, RIGHT, LEFT, CENTER]
        EMF [PAN, TILT, PONSIDE] [-127...127]
        POSITION [PAN, TILT, PONSIDE] [VAL]
        AUDIO TEMPO [67, 80, 100, 133, 200] (if BPM cannot be detected, this is estimated from power spectral density response)
        AUDIO MEAN [0...64] (the mean of the envelope over a 1.28sec window, max around 64 for very loud music, not updated when motors are moving)
        AUDIO RANGE [0...64] (dynamic range, max 64 for shouting, not updated when motors moving)
        AUDIO ENVELOPE [0...127] (near instantaneous log of the audio amplitude; commented out in code for reduction of data transfer)
        AUDIO BPM [VAL] (estimated beat interval in multiples of 5msec)
    * 
    */
    #endregion

    /// <summary>
    /// this does our sending and writes what we have sent to the terminal
    /// </summary>
    /// <param name="strCommand">Command to send to keepon</param>
    /// <param name="strDescription">Description to show in GUI terminal</param>
    public void sendString(string strCommand, string strDescription)
    {
        comport.Write(strCommand);
        Log(LogMsgType.Outgoing, "Sent: " + strDescription + " (" + strCommand + ")" + "\n");
    }

    #region Sounds
        private void cmdUpWakeSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 1;", "Play sound 1"); }
        private void cmdDownWakeSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 2;", "Play sound 2"); }
        private void cmdYawnDownSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 3;", "Play sound 3"); }
        private void cmdBootSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 4;", "Play sound 4"); }
        private void cmdSighSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 5;", "Play sound 5"); }
        private void cmdYawnUpSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 6;", "Play sound 6"); }
        private void cmdSleepSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 7;", "Play sound 7"); }
        private void cmdChirpSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 8;", "Play sound 8"); }
        private void cmdWhineSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 9;", "Play sound 9"); }
        private void cmdHeadHitSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 10;", "Play sound 10"); }
        private void cmdSquatSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 11;", "Play sound 11"); }
        private void cmdSneezeUpSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 12;", "Play sound 12"); }
        private void cmdSneezeDownSound_Click(object sender, EventArgs e) { sendString("SOUND PLAY 13;", "Play sound 13"); }
        private void cmdSound14_Click(object sender, EventArgs e) { sendString("SOUND PLAY 14;", "Play sound 14"); }
        private void cmdSound15_Click(object sender, EventArgs e) { sendString("SOUND PLAY 15;", "Play sound 15"); }
        private void cmdSoundStop_Click(object sender, EventArgs e) { sendString("SOUND STOP;", "Stop sound"); }
    #endregion

    #region Movements
        private void cmdBend_Click(object sender, EventArgs e)
        {
            sendString("MOVE SIDE LEFT;", "Move Left");
            Thread.Sleep(500);
            sendString("MOVE SIDE RIGHT;", "Move Right");
        }

        private void sldTilt_Scroll(object sender, EventArgs e) { nudTilt.Value = sldTilt.Value; }
        private void nudTilt_ValueChanged(object sender, EventArgs e)
        {
            int iTilt = (int)nudTilt.Value;
            sldTilt.Value = iTilt;
            SendTilt(iTilt);
        }
        private void SendTilt(int iTilt) { sendString("MOVE TILT " + iTilt + ";", "Changed tilt to: " + iTilt); }

        private void sldPan_Scroll(object sender, EventArgs e) { nudPan.Value = sldPan.Value; }
        private void nudPan_ValueChanged(object sender, EventArgs e)
        {
            int iPan = (int)nudPan.Value;
            sldPan.Value = iPan;
            SendPan(iPan);
        }
        private void SendPan(int iPan) { sendString("MOVE PAN " + iPan + ";", "Changed pan to: " + iPan); }

        private void sldSpeed_Scroll(object sender, EventArgs e) { nudSpeed.Value = sldSpeed.Value; }
        private void nudSpeed_ValueChanged(object sender, EventArgs e)
        {
            int iSpeed = (int)nudSpeed.Value;
            sldSpeed.Value = iSpeed;
            SendSpeed(iSpeed);
            Thread.Sleep(500);
        }
        private void SendSpeed(int iSpeed) 
        { 
            sendString("SPEED PAN " + iSpeed + ";", "Changed pan speed to: " + iSpeed);
            sendString("SPEED TILT " + iSpeed + ";", "Changed tilt speed to: " + iSpeed);
            sendString("SPEED PONSIDE " + iSpeed + ";", "Changed pon/side speed to: " + iSpeed);
        }

        private void sldLean_Scroll(object sender, EventArgs e)
        {
            //MOVE SIDE [CYCLE, CENTERFROMLEFT, RIGHT, CENTERFROMRIGHT, LEFT];
            //the scroll has 5 positions, so translate from a number to the correct command
            int iLean = sldLean.Value;
            switch (iLean)
            {
                case 1: sendString("MOVE SIDE LEFT;", "Lean left");                     break;
                case 2: sendString("MOVE SIDE CENTERFROMLEFT;", "Lean left-centre");    break;
                case 3: sendString("MOVE SIDE CYCLE;", "Lean cycle");                   break;
                case 4: sendString("MOVE SIDE CENTERFROMRIGHT;", "Lean right-centre");  break;
                case 5: sendString("MOVE SIDE RIGHT;", "Lean right");                   break;
            }       
        }

        private void sldHeight_Scroll(object sender, EventArgs e)
        {
            //MOVE PON [UP, HALFDOWN, DOWN, HALFUP];
            //translate from int 1-4 to position name
            int iHeight = sldHeight.Value;
            switch (iHeight)
            {
                case 1: sendString("MOVE PON DOWN;", "Height down");            break;
                case 2: sendString("MOVE PON HALFDOWN;", "Height half-down");   break;
                case 3: sendString("MOVE PON HALFUP;", "Height half-up");       break;
                case 4: sendString("MOVE PON UP;", "Height up");                break;
            }
        }

        private void cmdJump_Click(object sender, EventArgs e) { sendString("MOVE PON UP;", "Jump"); }
        private void cmdStopMove_Click(object sender, EventArgs e) { sendString("MOVE STOP;", "Move stopped"); }   
    #endregion

    //not quite sure what these do! maybe need to play loud music at it?
    #region Modes
        private void cmdDance_Click(object sender, EventArgs e) { sendString("MODE DANCE;", "Dance mode"); }
        private void cmdTouch_Click(object sender, EventArgs e) { sendString("MODE TOUCH;", "Touch mode"); }
        private void cmdSleep_Click(object sender, EventArgs e) { sendString("MODE SLEEP;", "Mode sleep"); }
        private void cmdTempo_Click(object sender, EventArgs e) { sendString("MODE TEMPO;", "Tempo mode"); }
    #endregion


        private void frmTerminal_Load(object sender, EventArgs e)
        {
            frmTerminal2 f2 = new frmTerminal2();
            f2.Show(this);
            f2.Location = new Point(this.Location.X, this.Location.Y + this.Size.Height);
        }

  }
}
