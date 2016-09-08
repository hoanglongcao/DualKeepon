using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Media;

namespace SerialPortTerminal
{
    public partial class frmKeeponExperiment : Form
    {
        #region Constructor
        private string userName;
        private string userGender;

        public frmKeeponExperiment(string userName, string userGender): base()
        {
            InitializeComponent();
            // Get User Info
            this.userName = userName;
            this.userGender = userGender;
            // Load experiment data
            loadExperimentData();
        }
        #endregion
        #region Global Variables
        public int numberofQuestions = 0;
        public int currentQuestion = 1; // change to test only
        public string currentQuestionPath;
        public string dataPath;

        public bool isbgWPlaySoundFinished = true;
        public bool isQuestionAnswered = false;
        public bool isKeeponRunning = false;

        public string userAnswer = "None";
        public string userDataPath;
        public string userData;

        public string keeponCommand;

        #endregion
        #region Local Methods
        private string checkIfImageExists(string path)
        {
            if (File.Exists(path + ".jpg")) return path + ".jpg";
            else if (File.Exists(path + ".jpeg")) return path + ".jpeg";
            else if (File.Exists(path + ".png")) return path + ".png";
            else if (File.Exists(path + ".gif")) return path + ".gif";
            else if (File.Exists(path + ".bmp")) return path + ".bmp";
            else return "None";
        }
        #endregion
        #region Game

        // Get Experiment Data
        private void loadExperimentData()
        {
            dataPath = System.IO.Path.GetDirectoryName(Application.ExecutablePath).ToString();
            userDataPath = dataPath + "\\_data\\users\\";
            // Loop until can't find the folder
            while (true)
            {
                if (Directory.Exists(dataPath + "\\_data\\question_" + (numberofQuestions + 1).ToString("D2")))
                {
                    numberofQuestions++;
                    label2.Text = "Number of questions: " + numberofQuestions.ToString();
                }
                else return;
            }
        }

        // Load new question: pictures, sounds
        private void loadNewQuestion()
        {
            // Reset flag
            isQuestionAnswered = false;
            userAnswer = "None";
            updateGUI();
            // Load path of the current question's folder
            currentQuestionPath = System.IO.Path.GetDirectoryName(Application.ExecutablePath).ToString() + "\\_data\\question_" + currentQuestion.ToString("D2");

            // Load question text
            labelQuestion.Text = File.ReadLines(currentQuestionPath + "\\question.txt").Skip(0).Take(1).First();

            // Load 2 images
            if (checkIfImageExists(currentQuestionPath + "\\1") != "None")
                pboxLeft.Image = Image.FromFile(checkIfImageExists(currentQuestionPath + "\\1"));
            else MessageBox.Show("No left image found. Check question " + currentQuestion.ToString("D2") + " folder!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            if (checkIfImageExists(currentQuestionPath + "\\2") != "None")
                pboxRight.Image = Image.FromFile(checkIfImageExists(currentQuestionPath + "\\2"));
            else MessageBox.Show("No right image found. Check question " + currentQuestion.ToString("D2") + " folder!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            // Load Sounds and Keepons Movements
            // Play a sound file and a movement in a different threat
            while (!isbgWPlaySoundFinished);
            backgroundWorkerPlaySound.RunWorkerAsync();

        }

        private void backgroundWorkerPlaySound_DoWork(object sender, DoWorkEventArgs e)
        {
            // Reset flag
            isbgWPlaySoundFinished = false;
            updateGUI();

            System.Threading.Thread.Sleep(1000); // can change the delay

            // Play sound files in order
            // List all audio file in the question folder - add more extenstion if possible
            var audioFiles = System.IO.Directory.GetFiles(currentQuestionPath + "\\_audio", "*.*", SearchOption.AllDirectories).Where(s => s.EndsWith(".mp3") || s.EndsWith(".wav") || s.EndsWith(".wma") || s.EndsWith(".w4a") || s.EndsWith(".ogg"));
            foreach (string s in audioFiles)
            {
                // Wait until Keepon finished running
                while(isKeeponRunning);
                System.Threading.Thread.Sleep(1000);
                // Make corresponding movements
                // Get filename without extension:
                string filename = s.Remove(s.Length - 4);
                // Paula
                if (filename.GetLast(5) == "Paula")
                {
                    label2.BeginInvoke(new MethodInvoker(() => { label2.Text = "Paula"; }));
                    keeponCommand = "PaulaSpeak";

                    bool isKeeponDone = false;
                    while (!isKeeponDone)
                    {
                        try
                        {
                            backgroundWorkerKeepon.RunWorkerAsync();
                            isKeeponDone = true;
                        }
                        catch (Exception)
                        {
                            isKeeponDone = false;
                        }
                    }
                }

                // Paul
                else if (filename.GetLast(4) == "Paul")
                {
                    label2.BeginInvoke(new MethodInvoker(() => { label2.Text = "Paul"; }));
                    keeponCommand = "PaulSpeak";
                    bool isKeeponDone = false;
                    while (!isKeeponDone)
                    {
                        try
                        {
                            backgroundWorkerKeepon.RunWorkerAsync();
                            isKeeponDone = true;
                        }
                        catch (Exception)
                        {
                            isKeeponDone = false;
                        }
                    }
                }

                // Play a sound
                SoundPlayer player = new SoundPlayer(s);
                player.PlaySync();

                
            }
            // Raise flag
            isbgWPlaySoundFinished = true;
            updateGUI();
        }

        // Perform Selection
        private void backgroundWorkerPerformSelection_DoWork(object sender, DoWorkEventArgs e)
        {
            // Reset flag
            isbgWPlaySoundFinished = false;
            updateGUI();

            if (userAnswer == "Right")
            {
                // Make movement
                label2.BeginInvoke(new MethodInvoker(() => { label2.Text = "Paula Selection"; }));
                keeponCommand = "PaulaChoice";
                bool isKeeponDone = false;
                while (!isKeeponDone)
                {
                    try
                    {
                        backgroundWorkerKeepon.RunWorkerAsync();
                        isKeeponDone = true;
                    }
                    catch (Exception)
                    {
                        isKeeponDone = false;
                    }
                }

                // Play a sound
                string paulaGreatChoice = System.IO.Path.GetDirectoryName(Application.ExecutablePath).ToString() + "\\_data\\_greatchoice_Paula.wav";
                SoundPlayer player = new SoundPlayer(paulaGreatChoice);
                player.PlaySync();
            }

            if (userAnswer == "Left")
            {
                // Make movement
                label2.BeginInvoke(new MethodInvoker(() => { label2.Text = "Paul Selection"; }));
                keeponCommand = "PaulChoice";
                bool isKeeponDone = false;
                while (!isKeeponDone)
                {
                    try
                    {
                        backgroundWorkerKeepon.RunWorkerAsync();
                        isKeeponDone = true;
                    }
                    catch (Exception)
                    {
                        isKeeponDone = false;
                    }
                }
                // Play a sound
                string paulGreatChoice = System.IO.Path.GetDirectoryName(Application.ExecutablePath).ToString() + "\\_data\\_greatchoice_Paul.wav";
                SoundPlayer player = new SoundPlayer(paulGreatChoice);
                player.PlaySync();

                
                
            }
            // Raise flag
            isbgWPlaySoundFinished = true;
            updateGUI();
            
        }

        private void sayGoodbye()
        {
            // Reset flag
            isQuestionAnswered = false;
            userAnswer = "None";
            updateGUI();

            labelQuestion.Text = "Thank you for your participation!";

            buttonNext.Text = "QUIT";
            buttonNext.BackColor = Color.Red;
            buttonNext.Visible = true;

            buttonLog.Visible = true;
            
            pboxLeft.Image = Image.FromFile(checkIfImageExists(dataPath+ "\\_data\\1"));
            pboxRight.Image = Image.FromFile(checkIfImageExists(dataPath + "\\_data\\2"));
            pboxLeft.BorderStyle = BorderStyle.None;
            pboxRight.BorderStyle = BorderStyle.None;

            System.Threading.Thread.Sleep(1000); // can change the delay
            while (!isbgWPlaySoundFinished);
            backgroundWorkerGoodbye.RunWorkerAsync();

        }
        private void backgroundWorkerGoodbye_DoWork(object sender, DoWorkEventArgs e)
        {
            // Reset flag
            isbgWPlaySoundFinished = false;
            updateGUI();

            // More here when required

            keeponCommand = "PaulSpeak";
            while (isKeeponRunning);
            System.Threading.Thread.Sleep(1000); // debug: wait for Keepon running
            bool isKeeponDone = false;
            while (!isKeeponDone)
            {
                try
                {
                    backgroundWorkerKeepon.RunWorkerAsync();
                    isKeeponDone = true;
                }
                catch (Exception)
                {
                    isKeeponDone = false;
                }
            }
            string paulGoodbye = System.IO.Path.GetDirectoryName(Application.ExecutablePath).ToString() + "\\_data\\_thankyou_Paul.wav";
            SoundPlayer player = new SoundPlayer(paulGoodbye);
            player.PlaySync();
            // Raise flag
            isbgWPlaySoundFinished = true;
            updateGUI();
        }

        // Thread for controlling Keepon
        private void backgroundWorkerKeepon_DoWork(object sender, DoWorkEventArgs e)
        {
            isKeeponRunning = true;
            switch (keeponCommand)
            {
                case "PaulaSpeak":
                    try { (this.Owner as frmTerminal2).KeeponRightSpeak(); }
                    catch (Exception)
                    {
                        MessageBox.Show("Cannot control Keepon RIGHT", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    break;

                case "PaulSpeak":
                    try { (this.Owner as frmTerminal2).KeeponLeftSpeak(); }
                    catch (Exception)
                    {
                        MessageBox.Show("Cannot control Keepon LEFT", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    break;

                case "PaulaChoice":
                    try { (this.Owner as frmTerminal2).KeeponRightChoice(); }
                    catch (Exception)
                    {
                        MessageBox.Show("Cannot control Keepon RIGHT", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    break;

                case "PaulChoice":
                    try { (this.Owner as frmTerminal2).KeeponLeftChoice(); }
                    catch (Exception)
                    {
                        MessageBox.Show("Cannot control Keepon LEFT", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    break;

            }
            isKeeponRunning = false;
        }


        
        // Update properties of all GUI components
        private void updateGUI()
        {
            try
            {
                if (buttonNext.Text == "NEXT") buttonNext.Visible = isQuestionAnswered;
                else buttonNext.Visible = true;

                if (userAnswer == "Left") pboxLeft.BorderStyle = BorderStyle.FixedSingle;
                else pboxLeft.BorderStyle = BorderStyle.None;

                if (userAnswer == "Right") pboxRight.BorderStyle = BorderStyle.FixedSingle;
                else pboxRight.BorderStyle = BorderStyle.None;

                // Debug
                labelDebug.Text = isbgWPlaySoundFinished.ToString() + isQuestionAnswered.ToString();
                labelAnswer.Text = userAnswer;

                if (!isQuestionAnswered)
                {
                    //buttonNext.BackColor = default(Color);
                }
                else
                {
                    //buttonNext.BackColor = System.Drawing.Color.Lime;
                }
            }
            catch (InvalidOperationException)
            {
                buttonNext.BeginInvoke(new MethodInvoker(() =>
                {
                    if (buttonNext.Text == "NEXT") buttonNext.Visible = isQuestionAnswered;
                    else buttonNext.Visible = true;
                    //if (!isQuestionAnswered) buttonNext.BackColor = default(Color);
                    //else buttonNext.BackColor = System.Drawing.Color.Lime;
                }));

                pboxLeft.BeginInvoke(new MethodInvoker(() =>
                {
                    if (userAnswer == "Left") pboxLeft.BorderStyle = BorderStyle.FixedSingle;
                    else pboxLeft.BorderStyle = BorderStyle.None;
                }));
                
                pboxRight.BeginInvoke(new MethodInvoker(() =>
                {
                    if (userAnswer == "Right") pboxRight.BorderStyle = BorderStyle.FixedSingle;
                    else pboxRight.BorderStyle = BorderStyle.None;
                }));

                //Debug
                labelDebug.BeginInvoke(new MethodInvoker(() =>
                {
                    labelDebug.Text = isbgWPlaySoundFinished.ToString() + isQuestionAnswered.ToString();
                }));
                labelAnswer.BeginInvoke(new MethodInvoker(() =>
                {
                    labelAnswer.Text = userAnswer;
                }));
            }
        
        }

       

        #endregion
 
        #region GUI Components Actions

        private void buttonNext_Click(object sender, EventArgs e)
        {
            if (buttonNext.Text == "NEXT")
            {
                // Check answer and select Left or Right Keepon
                isbgWPlaySoundFinished = false;
                //updateGUI();
                System.Threading.Thread.Sleep(1000);
                bool isPerformSelectionDone = false;
                while (!isPerformSelectionDone)
                {
                    try
                    {
                        backgroundWorkerPerformSelection.RunWorkerAsync(); // run on another threat
                        isPerformSelectionDone = true;
                    }
                    catch (Exception)
                    {
                    }
                }
                
                while (!isbgWPlaySoundFinished) ;

                //Write user data file
                if (userAnswer == "Left")
                    writeData(userDataPath + userName + "_" + userGender + ".txt","Question "+currentQuestion.ToString()+": "+ "Left(Paul)");
                else if (userAnswer == "Right")
                    writeData(userDataPath + userName + "_" + userGender + ".txt", "Question " + currentQuestion.ToString() + ": " + "Right(Paula)");
                
                //Reset - fixed bug
                pboxLeft.BorderStyle = BorderStyle.FixedSingle;
                pboxRight.BorderStyle = BorderStyle.FixedSingle;

                // Next question and load images and sounds
                currentQuestion++;
                if (currentQuestion <= numberofQuestions)   loadNewQuestion();
                else sayGoodbye();
            }
            else //QUIT
                if (isbgWPlaySoundFinished) this.Close();
        }

        private void pboxLeft_Click(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished)
            {
                userAnswer = "Left";
                isQuestionAnswered = true;
                updateGUI();
            }
        }

        private void pboxRight_Click(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished)
            {
                userAnswer = "Right";
                isQuestionAnswered = true;
                updateGUI();
            }
        }

        private void pboxRight_MouseEnter(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished) Cursor = Cursors.Hand;
        }

        private void pboxRight_MouseLeave(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished) Cursor = Cursors.Arrow;
        }

        private void pboxLeft_MouseEnter(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished) Cursor = Cursors.Hand;
        }

        private void pboxLeft_MouseLeave(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished) Cursor = Cursors.Arrow;
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            System.Threading.Thread.Sleep(1000); // can change the delay
            buttonStart.Visible = false;
            buttonNext.Visible = true;
            // Load the first question. Next questions are loaded by clicking NEXT button
            loadNewQuestion();
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            if (isbgWPlaySoundFinished) this.Close();
        }

        private void buttonLog_Click(object sender, EventArgs e)
        {
            try
            {
                string log = File.ReadAllText(userDataPath + userName + "_" + userGender + ".txt");
                MessageBox.Show(log, "User Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception)
            {
                MessageBox.Show("No data found", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        #endregion
        #region Log
        private void writeData(string filename, string text)
        {
           File.AppendAllText(filename, text + Environment.NewLine);
        }
        #endregion

    }
    # region Extra Class Functions
    // Add extra functions for String 
    public static class StringExtension
    {
       public static string GetLast(this string source, int tail_length)
       {
           if (tail_length >= source.Length)
               return source;
           return source.Substring(source.Length - tail_length);
       }
   }
    #endregion
}

