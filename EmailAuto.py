fromaddr = "spartacus.automation@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Status2013")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
 
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = ", ".join(TO)
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>!"""
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Status2013")


    server.sendmail(FROM, TO, MESSAGE.as_string())
    server.quit()
    
email_content = """
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table {  
    color: #333;
    font-family: Helvetica, Arial, sans-serif;
    width: 640px; 
    border-collapse: 
    collapse; border-spacing: 0; 
}

td, th {  
    border: 1px solid transparent; /* No more visible border */
    height: 30px; 
    transition: all 0.3s;  /* Simple transition for hover effect */
}

th {  
    background: #DFDFDF;  /* Darken header a bit */
    font-weight: bold;
}

td {  
    background: #FAFAFA;
    text-align: center;
}

/* Cells in even rows (2,4,6...) are one color */        
tr:nth-child(even) td { background: #F1F1F1; }   

/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */        
tr:nth-child(odd) td { background: #FEFEFE; }  

tr td:hover { background: #666; color: #FFF; }  
/* Hover cell effect! */
  </style>
</head>
<body>

    <p>Hi Friendly investor ! Here is a less ugly mail for you ! <3 <3 </p>
  <table border="1">
  <tr>
    <th>Date</th>
    <th>Gasoil</th>
    <th>Bund</th>
    <th>Cocoa</th>
    <th>Cofee</th>
    
  </tr>
  <tr>
  	<td> 18 janvier </td>
    <td background="#00FF00"> Long</td>
    <td>  Flat </td>
    <td bgcolor="#FF0000"> Short</td>
    <td bgcolor="#00FF00"> Long</td>
  </tr>
</table>

<p>As a reminder, here are a few informations you could consider interesting about our latest trades<p> 

  <table border="1">
  <tr>
    <th>Date</th>
    
    <th>Gasoil Prediction </th>
    <th>Gasoil Real </th>
    
    <th>Bund Prediction</th>
    <th>Bund Real</th>
    
    <th>Cocoa Prediction</th>
    <th>Cocoa Real 
    
    <th>Coffee Prediction </th>
    <th>Coffee Real </th>
    
  </tr>
  <tr>
  	<td> 17 decembre </td>
    <td bgcolor="#00FF00"> Long</td>
    <td> +3 </td>
    <td>  Flat </td>
    <td> -3 </td>
    <td bgcolor="#FF0000"> Short</td>
    <td> +3 </td>
    <td bgcolor="#00FF00"> Long</td>
    <td> -3 </td>
  </tr>
  
  <tr>
  	<td> 3 janvier </td>
    <td bgcolor="#FF0000"> Short</td>
    <td> +3 </td>
    <td>  Flat </td>
    <td> -3 </td>
    <td>  Flat </td>
    <td> -3 </td>
    <td bgcolor="#00FF00"> Long</td>
    <td> +3 </td>
  </tr>
</table>

<p>Here are our ongoing PNL and sharp :) </p>
<table border="1">
  <tr>
    
    <th>Previous month PNL </th>
    <th>Previous month sharp </th>
    
    <th>6 months PNL</th>
    <th>6 months sharp </th>
    
    <th>1 year PNL</th>
    <th>1 year sharp </th>
    
  </tr>
  <tr>
    
    <td>1.2 </td>
    <td>42 </td>
    
    <td>1.5</td>
    <td> 42</td>
    
    <td>6</td>
    <td>42</td>

    
  </tr>
</table>

<p> If you have any problem visualizing this mail, please send us a  <a href="mailto:cedric.mavoungou@email.com?subject=I am not happy% &body=Easy%20de%20faire%20des%20mails%20pas%20degeux">mail</a>  </p>
</body>
"""
 
def style_generator():
    pass
    
TO  = ['maximilien.pel
       letier@gmail.com']
FROM ='maximilien.pelletier@gmail.com'
 
py_mail("Test mail HTML + joli tableau", email_content, TO, FROM)
