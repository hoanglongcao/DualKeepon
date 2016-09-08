namespace SerialPortTerminal
{
    partial class frmKeeponExperiment
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.pboxLeft = new System.Windows.Forms.PictureBox();
            this.pboxRight = new System.Windows.Forms.PictureBox();
            this.labelQuestion = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.buttonStart = new System.Windows.Forms.Button();
            this.buttonNext = new System.Windows.Forms.Button();
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelDebug = new System.Windows.Forms.Label();
            this.buttonLog = new System.Windows.Forms.Button();
            this.labelAnswer = new System.Windows.Forms.Label();
            this.backgroundWorkerPlaySound = new System.ComponentModel.BackgroundWorker();
            this.backgroundWorkerPerformSelection = new System.ComponentModel.BackgroundWorker();
            this.backgroundWorkerGoodbye = new System.ComponentModel.BackgroundWorker();
            this.backgroundWorkerKeepon = new System.ComponentModel.BackgroundWorker();
            this.tableLayoutPanel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pboxLeft)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pboxRight)).BeginInit();
            this.SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 5;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 7.751938F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 38.37209F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 7.751938F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 38.37209F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 7.751938F));
            this.tableLayoutPanel1.Controls.Add(this.pboxLeft, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.pboxRight, 3, 1);
            this.tableLayoutPanel1.Controls.Add(this.labelQuestion, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.label2, 0, 2);
            this.tableLayoutPanel1.Controls.Add(this.buttonStart, 2, 1);
            this.tableLayoutPanel1.Controls.Add(this.buttonNext, 2, 2);
            this.tableLayoutPanel1.Controls.Add(this.buttonExit, 4, 0);
            this.tableLayoutPanel1.Controls.Add(this.labelDebug, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.buttonLog, 3, 2);
            this.tableLayoutPanel1.Controls.Add(this.labelAnswer, 4, 1);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 3;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 80F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(1220, 481);
            this.tableLayoutPanel1.TabIndex = 0;
            // 
            // pboxLeft
            // 
            this.pboxLeft.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pboxLeft.Location = new System.Drawing.Point(97, 51);
            this.pboxLeft.Name = "pboxLeft";
            this.pboxLeft.Size = new System.Drawing.Size(462, 378);
            this.pboxLeft.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pboxLeft.TabIndex = 1;
            this.pboxLeft.TabStop = false;
            this.pboxLeft.Click += new System.EventHandler(this.pboxLeft_Click);
            this.pboxLeft.MouseEnter += new System.EventHandler(this.pboxLeft_MouseEnter);
            this.pboxLeft.MouseLeave += new System.EventHandler(this.pboxLeft_MouseLeave);
            // 
            // pboxRight
            // 
            this.pboxRight.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pboxRight.Location = new System.Drawing.Point(659, 51);
            this.pboxRight.Name = "pboxRight";
            this.pboxRight.Size = new System.Drawing.Size(462, 378);
            this.pboxRight.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pboxRight.TabIndex = 2;
            this.pboxRight.TabStop = false;
            this.pboxRight.Click += new System.EventHandler(this.pboxRight_Click);
            this.pboxRight.MouseEnter += new System.EventHandler(this.pboxRight_MouseEnter);
            this.pboxRight.MouseLeave += new System.EventHandler(this.pboxRight_MouseLeave);
            // 
            // labelQuestion
            // 
            this.labelQuestion.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.labelQuestion.AutoSize = true;
            this.tableLayoutPanel1.SetColumnSpan(this.labelQuestion, 3);
            this.labelQuestion.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelQuestion.Location = new System.Drawing.Point(97, 0);
            this.labelQuestion.Name = "labelQuestion";
            this.labelQuestion.Size = new System.Drawing.Size(1024, 48);
            this.labelQuestion.TabIndex = 3;
            this.labelQuestion.Text = "Click START to begin";
            this.labelQuestion.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.tableLayoutPanel1.SetColumnSpan(this.label2, 2);
            this.label2.Location = new System.Drawing.Point(3, 432);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(54, 17);
            this.label2.TabIndex = 4;
            this.label2.Text = "Debug:";
            this.label2.Visible = false;
            // 
            // buttonStart
            // 
            this.buttonStart.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.buttonStart.AutoSize = true;
            this.buttonStart.BackColor = System.Drawing.Color.Lime;
            this.buttonStart.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonStart.Location = new System.Drawing.Point(565, 196);
            this.buttonStart.Name = "buttonStart";
            this.buttonStart.Size = new System.Drawing.Size(88, 88);
            this.buttonStart.TabIndex = 5;
            this.buttonStart.Text = "START";
            this.buttonStart.UseVisualStyleBackColor = false;
            this.buttonStart.Click += new System.EventHandler(this.buttonStart_Click);
            // 
            // buttonNext
            // 
            this.buttonNext.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.buttonNext.BackColor = System.Drawing.Color.Lime;
            this.buttonNext.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonNext.Location = new System.Drawing.Point(565, 435);
            this.buttonNext.Name = "buttonNext";
            this.buttonNext.Size = new System.Drawing.Size(88, 43);
            this.buttonNext.TabIndex = 0;
            this.buttonNext.Text = "NEXT";
            this.buttonNext.UseVisualStyleBackColor = false;
            this.buttonNext.Visible = false;
            this.buttonNext.Click += new System.EventHandler(this.buttonNext_Click);
            // 
            // buttonExit
            // 
            this.buttonExit.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.buttonExit.BackColor = System.Drawing.Color.Red;
            this.buttonExit.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonExit.Location = new System.Drawing.Point(1136, 3);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(81, 42);
            this.buttonExit.TabIndex = 6;
            this.buttonExit.Text = "EXIT";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelDebug
            // 
            this.labelDebug.AutoSize = true;
            this.labelDebug.Location = new System.Drawing.Point(3, 48);
            this.labelDebug.Name = "labelDebug";
            this.labelDebug.Size = new System.Drawing.Size(50, 17);
            this.labelDebug.TabIndex = 7;
            this.labelDebug.Text = "Debug";
            this.labelDebug.Visible = false;
            // 
            // buttonLog
            // 
            this.buttonLog.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.buttonLog.BackColor = System.Drawing.Color.MediumTurquoise;
            this.buttonLog.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonLog.Location = new System.Drawing.Point(659, 435);
            this.buttonLog.Name = "buttonLog";
            this.buttonLog.Size = new System.Drawing.Size(462, 43);
            this.buttonLog.TabIndex = 8;
            this.buttonLog.Text = "View Log";
            this.buttonLog.UseVisualStyleBackColor = false;
            this.buttonLog.Visible = false;
            this.buttonLog.Click += new System.EventHandler(this.buttonLog_Click);
            // 
            // labelAnswer
            // 
            this.labelAnswer.AutoSize = true;
            this.labelAnswer.Location = new System.Drawing.Point(1127, 48);
            this.labelAnswer.Name = "labelAnswer";
            this.labelAnswer.Size = new System.Drawing.Size(58, 17);
            this.labelAnswer.TabIndex = 9;
            this.labelAnswer.Text = "Answer:";
            this.labelAnswer.Visible = false;
            // 
            // backgroundWorkerPlaySound
            // 
            this.backgroundWorkerPlaySound.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorkerPlaySound_DoWork);
            // 
            // backgroundWorkerPerformSelection
            // 
            this.backgroundWorkerPerformSelection.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorkerPerformSelection_DoWork);
            // 
            // backgroundWorkerGoodbye
            // 
            this.backgroundWorkerGoodbye.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorkerGoodbye_DoWork);
            // 
            // backgroundWorkerKeepon
            // 
            this.backgroundWorkerKeepon.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorkerKeepon_DoWork);
            // 
            // frmKeeponExperiment
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1220, 481);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Name = "frmKeeponExperiment";
            this.Text = "Keepon Experiment";
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pboxLeft)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pboxRight)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.PictureBox pboxLeft;
        private System.Windows.Forms.PictureBox pboxRight;
        private System.Windows.Forms.Label labelQuestion;
        private System.ComponentModel.BackgroundWorker backgroundWorkerPlaySound;
        private System.Windows.Forms.Button buttonStart;
        private System.Windows.Forms.Label label2;
        private System.ComponentModel.BackgroundWorker backgroundWorkerPerformSelection;
        private System.ComponentModel.BackgroundWorker backgroundWorkerGoodbye;
        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Label labelDebug;
        private System.Windows.Forms.Button buttonLog;
        private System.Windows.Forms.Label labelAnswer;
        private System.ComponentModel.BackgroundWorker backgroundWorkerKeepon;
    }
}