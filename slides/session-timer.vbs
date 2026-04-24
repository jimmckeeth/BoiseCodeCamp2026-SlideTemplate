' --- Configuration ---
totalMinutes = 45
blinkOnceAt = 10
blinkEverySecondAt = 5
' ---------------------

Set objShell = CreateObject("WScript.Shell")

' Build the PowerShell command string
' We inject the VBScript variables directly into the PowerShell string
psCode = "Add-Type -AssemblyName System.Windows.Forms, System.Drawing; " & _
         "$f = New-Object Windows.Forms.Form; $f.Text = '" & totalMinutes & "m Timer'; $f.TopMost = $true; " & _
         "$f.Width = 250; $f.Height = 130; $f.FormBorderStyle = 'FixedToolWindow'; $f.StartPosition = 'CenterScreen'; " & _
         "$f.BackColor = [System.Drawing.Color]::FromArgb(32, 32, 32); " & _
         "$l = New-Object Windows.Forms.Label; $l.Dock = 'Fill'; $l.TextAlign = 'MiddleCenter'; " & _
         "$l.ForeColor = [System.Drawing.Color]::White; $l.Font = New-Object Drawing.Font('Segoe UI', 36, [Drawing.FontStyle]::Bold); " & _
         "$f.Controls.Add($l); $endTime = [DateTime]::Now.AddMinutes(" & totalMinutes & "); " & _
         "$t = New-Object Windows.Forms.Timer; $t.Interval = 1000; " & _
         "$t.Add_Tick({ " & _
         "  $rem = $endTime - [DateTime]::Now; $s = [Math]::Floor($rem.TotalSeconds); " & _
         "  if ($s -lt 0) { " & _
         "    $l.Text = '00:00'; $l.ForeColor = [System.Drawing.Color]::Red; $t.Stop(); [System.Media.SystemSounds]::Exclamation.Play() " & _
         "  } else { " & _
         "    $l.Text = $rem.ToString('mm\:ss'); " & _
         "    if ($s -le " & (blinkEverySecondAt * 60) & ") { " & _
         "      if ($s % 2 -eq 0) { $l.ForeColor = [System.Drawing.Color]::Yellow } else { $l.ForeColor = [System.Drawing.Color]::White } " & _
         "    } elseif ($s -eq " & (blinkOnceAt * 60) & ") { " & _
         "      $l.ForeColor = [System.Drawing.Color]::Yellow " & _
         "    } else { " & _
         "      $l.ForeColor = [System.Drawing.Color]::White " & _
         "    } " & _
         "  } " & _
         "}); $f.Add_Shown({ $t.Start() }); $f.ShowDialog()"

' Run powershell hidden (0), don't wait for exit (False)
objShell.Run "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -Command ""& {" & psCode & "}""", 0, False
