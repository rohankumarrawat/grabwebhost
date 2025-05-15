msgg=[]
import smtplib
f=open('C:\\Users\\sajid ali\\OneDrive\\Desktop\\output.txt','r')

data=f.readlines()
for i in range(30):
    msgg.append(data[i].replace("\n","").replace(",",""))
from email.message import EmailMessage
msg = EmailMessage()
msg['To']=msgg
msg['Subject'] = 'Here is my newsletter'
msg['From'] = "info@grabwebhost.in" 

msg.set_content(''' 
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <!--[if gte mso 9]>
    <xml>
      <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="x-apple-disable-message-reformatting">
    <!--[if !mso]><!-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
    <title></title>

    <style type="text/css">
        @media only screen and (min-width: 620px) {
            .u-row {
                width: 600px !important;
            }

            .u-row .u-col {
                vertical-align: top;
            }

            .u-row .u-col-100 {
                width: 600px !important;
            }

        }

        @media (max-width: 620px) {
            .u-row-container {
                max-width: 100% !important;
                padding-left: 0px !important;
                padding-right: 0px !important;
            }

            .u-row .u-col {
                min-width: 320px !important;
                max-width: 100% !important;
                display: block !important;
            }

            .u-row {
                width: 100% !important;
            }

            .u-col {
                width: 100% !important;
            }

            .u-col>div {
                margin: 0 auto;
            }
        }

        body {
            margin: 0;
            padding: 0;
        }

        table,
        tr,
        td {
            vertical-align: top;
            border-collapse: collapse;
        }

        p {
            margin: 0;
        }

        .ie-container table,
        .mso-container table {
            table-layout: fixed;
        }

        * {
            line-height: inherit;
        }

        a[x-apple-data-detectors='true'] {
            color: inherit !important;
            text-decoration: none !important;
        }

        table,
        td {
            color: #000000;
        }

        #u_body a {
            color: #0000ee;
            text-decoration: underline;
        }

        @media (max-width: 480px) {
            #u_content_heading_1 .v-container-padding-padding {
                padding: 70px 10px 36px !important;
            }

            #u_content_heading_1 .v-font-size {
                font-size: 36px !important;
            }

            #u_content_heading_1 .v-line-height {
                line-height: 100% !important;
            }

            #u_content_image_1 .v-src-width {
                width: auto !important;
            }

            #u_content_image_1 .v-src-max-width {
                max-width: 100% !important;
            }

            #u_content_button_1 .v-container-padding-padding {
                padding: 28px 10px 101px !important;
            }

            #u_content_button_1 .v-size-width {
                width: 71% !important;
            }

            #u_content_button_1 .v-padding {
                padding: 10px 20px !important;
            }

            #u_content_heading_2 .v-container-padding-padding {
                padding: 40px 10px 10px !important;
            }

            #u_content_heading_2 .v-font-size {
                font-size: 30px !important;
            }

            #u_content_divider_1 .v-container-padding-padding {
                padding: 1px 10px 24px !important;
            }

            #u_content_image_2 .v-src-width {
                width: auto !important;
            }

            #u_content_image_2 .v-src-max-width {
                max-width: 80% !important;
            }

            #u_content_button_3 .v-size-width {
                width: 60% !important;
            }

            #u_content_image_3 .v-src-width {
                width: auto !important;
            }

            #u_content_image_3 .v-src-max-width {
                max-width: 82% !important;
            }

            #u_content_button_4 .v-size-width {
                width: 60% !important;
            }

            #u_content_image_4 .v-src-width {
                width: auto !important;
            }

            #u_content_image_4 .v-src-max-width {
                max-width: 80% !important;
            }

            #u_content_button_2 .v-size-width {
                width: 60% !important;
            }

            #u_content_heading_6 .v-font-size {
                font-size: 30px !important;
            }

            #u_content_button_6 .v-size-width {
                width: 70% !important;
            }
        }
    </style>



</head>

<body class="clean-body u_body"
    style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #e7e7e7;color: #000000">
    <!--[if IE]><div class="ie-container"><![endif]-->
    <!--[if mso]><div class="mso-container"><![endif]-->
    <table id="u_body"
        style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #e7e7e7;width:100%"
        cellpadding="0" cellspacing="0">
        <tbody>
            <tr style="vertical-align: top">
                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #e7e7e7;"><![endif]-->



                    <!--[if gte mso 9]>
          <table cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto;min-width: 320px;max-width: 600px;">
            <tr>
              <td background="https://cdn.templates.unlayer.com/assets/1689837494521-Rectangle%202%20copy.png" valign="top" width="100%">
          <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width: 600px;">
            <v:fill type="frame" src="https://cdn.templates.unlayer.com/assets/1689837494521-Rectangle%202%20copy.png" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">
          <![endif]-->

                    <div class="u-row-container"
                        style="padding: 0px;background-image: url('https://cdn.templates.unlayer.com/assets/1689837494521-Rectangle%202%20copy.png');background-repeat: no-repeat;background-position: center top;background-color: transparent">
                        <div class="u-row"
                            style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                            <div
                                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-image: url('https://cdn.templates.unlayer.com/assets/1689837494521-Rectangle%202%20copy.png');background-repeat: no-repeat;background-position: center top;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                                <div class="u-col u-col-100"
                                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                    <div style="height: 100%;width: 100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div
                                            style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
                                            <!--<![endif]-->

                                            <table id="u_content_heading_1"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:70px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">
                                                            &nbsp;
                                                            &nbsp;
                                                            <h1 class="v-line-height v-font-size"
                                                                style="margin: 0px; color: #ffffff; line-height: 120%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 46px; font-weight: 400;">
                                                                <img src="https://grabwebhost.in/static/images/logolight.png"
                                                                    widht=30 height=30><br>Be on Google
                                                            </h1>
                                                            &nbsp;
                                                            <h3
                                                                style="margin: 0px; color: #ffffff; line-height: 100%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 18px; font-weight: 400;">
                                                                Get Your<span style="color:yellow"> Portfolio</span>
                                                                Site with Free <span style="color:yellow"> Domain and
                                                                    hosting </span></h3>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_image_1"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:70px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                border="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center">

                                                                            <img align="center" border="0"
                                                                                src="https://grabwebhost.in/static/temp.png"
                                                                                height=500 alt="image" title="image"
                                                                                style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;float: none;width: 77%;max-width: 446.6px;"
                                                                                width="446.6"
                                                                                class="v-src-width v-src-max-width">

                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:32px 50px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <div class="v-line-height v-font-size"
                                                                style="font-size: 16px; line-height: 140%; text-align: center; word-wrap: break-word;">
                                                                <p style="line-height: 140%;">Get Your dream Website by
                                                                    us at most affordable price ,We have already
                                                                    PreBuild Dynamic/Static website with us, join our
                                                                    3rd Aniversary for the sale!
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_button_1"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:28px 10px 90px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
                                                            <div align="center">
                                                                <!--[if mso]><table border="0" cellspacing="0" cellpadding="0"><tr><td align="center" bgcolor="#a951a3" style="padding:10px 20px;" valign="top"><![endif]-->
                                                                <a href="https://grabwebhost.in" target="_blank"
                                                                    class="v-button v-size-width v-font-size"
                                                                    style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #a951a3; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 15px;">
                                                                    <span class="v-line-height v-padding"
                                                                        style="display:block;padding:10px 20px;line-height:120%;"><span
                                                                            style="line-height: 18px;">Visit
                                                                            Now</span></span>
                                                                </a>
                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_heading_2"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:40px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <h1 class="v-line-height v-font-size"
                                                                style="margin: 0px; color: #ffffff; line-height: 120%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 37px; font-weight: 400;">
                                                                Our WorkFlow<br></h1>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_divider_1"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:1px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table height="0px" align="center" border="0"
                                                                cellpadding="0" cellspacing="0" width="34%"
                                                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 10px solid #a951a3;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td
                                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                            <span>&nbsp;</span>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_image_2"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                border="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center">

                                                                            <img align="center" border="0"
                                                                                src="https://cdn.templates.unlayer.com/assets/1689837389356-Layer%201.png"
                                                                                alt="image" title="image"
                                                                                style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 307px;"
                                                                                width="307"
                                                                                class="v-src-width v-src-max-width">

                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <h1 class="v-line-height v-font-size"
                                                                style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 29px; font-weight: 400;">
                                                                Visit Website</h1>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_button_3"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
                                                            <div align="center">
                                                                <!--[if mso]><table border="0" cellspacing="0" cellpadding="0"><tr><td align="center" bgcolor="#a951a3" style="padding:10px 20px;" valign="top"><![endif]-->
                                                                <a href="https://grabwebhost.in/webdev" target="_blank"
                                                                    class="v-button v-size-width v-font-size"
                                                                    style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #a951a3; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 15px;">
                                                                    <span class="v-line-height v-padding"
                                                                        style="display:block;padding:10px 20px;line-height:120%;"><span
                                                                            style="line-height: 18px;">Check
                                                                            Now</span></span>
                                                                </a>
                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_image_3"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                border="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center">

                                                                            <img align="center" border="0"
                                                                                src="https://cdn.templates.unlayer.com/assets/1689837704452-Layer%203.png"
                                                                                alt="image" title="image"
                                                                                style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 307px;"
                                                                                width="307"
                                                                                class="v-src-width v-src-max-width">

                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <h1 class="v-line-height v-font-size"
                                                                style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 29px; font-weight: 400;">
                                                                Select Template</h1>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_button_4"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
                                                            <div align="center">
                                                                <!--[if mso]><table border="0" cellspacing="0" cellpadding="0"><tr><td align="center" bgcolor="#a951a3" style="padding:10px 20px;" valign="top"><![endif]-->
                                                                <a href="https://grabwebhost.in/prebuild/"
                                                                    target="_blank"
                                                                    class="v-button v-size-width v-font-size"
                                                                    style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #a951a3; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 15px;">
                                                                    <span class="v-line-height v-padding"
                                                                        style="display:block;padding:10px 20px;line-height:120%;"><span
                                                                            style="line-height: 18px;">Select Now
                                                                            Now</span></span>
                                                                </a>
                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_image_4"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                border="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center">

                                                                            <img align="center" border="0"
                                                                                src="https://cdn.templates.unlayer.com/assets/1689837772144-Layer%202.png"
                                                                                alt="image" title="image"
                                                                                style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 307px;"
                                                                                width="307"
                                                                                class="v-src-width v-src-max-width">

                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <h1 class="v-line-height v-font-size"
                                                                style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-family: book antiqua,palatino; font-size: 29px; font-weight: 400;">
                                                                Next Steps</h1>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table id="u_content_button_2"
                                                style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 30px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
                                                            <div align="center">
                                                                <!--[if mso]><table border="0" cellspacing="0" cellpadding="0"><tr><td align="center" bgcolor="#a951a3" style="padding:10px 20px;" valign="top"><![endif]-->
                                                                <a href="https://grabwebhost.in/contact" target="_blank"
                                                                    class="v-button v-size-width v-font-size"
                                                                    style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #a951a3; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 15px;">
                                                                    <span class="v-line-height v-padding"
                                                                        style="display:block;padding:10px 20px;line-height:120%;"><span
                                                                            style="line-height: 18px;">Contact
                                                                            Us</span></span>
                                                                </a>
                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div><!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>

                    <!--[if gte mso 9]>
          </v:textbox></v:rect>
        </td>
        </tr>
        </table>
        <![endif]-->





                    <div class="u-row-container" style="padding: 0px;background-color: transparent">
                        <div class="u-row"
                            style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                            <div
                                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #1b2e35;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                                <div class="u-col u-col-100"
                                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                    <div
                                        style="background-color: #1b2e35;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div
                                            style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <!--<![endif]-->





                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div><!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>





                    <div class="u-row-container" style="padding: 0px;background-color: transparent">
                        <div class="u-row"
                            style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                            <div
                                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #ffffff;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                                <div class="u-col u-col-100"
                                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                    <div
                                        style="background-color: #ffffff;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div
                                            style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <!--<![endif]-->

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:60px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <div align="center">
                                                                <div style="display: table; max-width:187px;">
                                                                    <!--[if (mso)|(IE)]><table width="187" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:187px;"><tr><![endif]-->


                                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 15px;" valign="top"><![endif]-->
                                                                    <table align="left" border="0" cellspacing="0"
                                                                        cellpadding="0" width="32" height="32"
                                                                        style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top">
                                                                                <td align="left" valign="middle"
                                                                                    style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                                                    <a href="https://facebook.com/grabwebhost"
                                                                                        title="Facebook"
                                                                                        target="_blank">
                                                                                        <img src="https://cdn.tools.unlayer.com/social/icons/rounded-black/facebook.png"
                                                                                            alt="Facebook"
                                                                                            title="Facebook" width="32"
                                                                                            style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                                                    </a>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 15px;" valign="top"><![endif]-->
                                                                    <table align="left" border="0" cellspacing="0"
                                                                        cellpadding="0" width="32" height="32"
                                                                        style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top">
                                                                                <td align="left" valign="middle"
                                                                                    style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                                                    <a href="https://twitter.com/grabwebhost"
                                                                                        title="Twitter" target="_blank">
                                                                                        <img src="https://cdn.tools.unlayer.com/social/icons/rounded-black/twitter.png"
                                                                                            alt="Twitter"
                                                                                            title="Twitter" width="32"
                                                                                            style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                                                    </a>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 15px;" valign="top"><![endif]-->
                                                                    <table align="left" border="0" cellspacing="0"
                                                                        cellpadding="0" width="32" height="32"
                                                                        style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top">
                                                                                <td align="left" valign="middle"
                                                                                    style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                                                    <a href="https://linkedin.com/grabwebhost"
                                                                                        title="LinkedIn"
                                                                                        target="_blank">
                                                                                        <img src="https://cdn.tools.unlayer.com/social/icons/rounded-black/linkedin.png"
                                                                                            alt="LinkedIn"
                                                                                            title="LinkedIn" width="32"
                                                                                            style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                                                    </a>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
                                                                    <table align="left" border="0" cellspacing="0"
                                                                        cellpadding="0" width="32" height="32"
                                                                        style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top">
                                                                                <td align="left" valign="middle"
                                                                                    style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                                                    <a href="https://instagram.com/grabwebhost"
                                                                                        title="Instagram"
                                                                                        target="_blank">
                                                                                        <img src="https://cdn.tools.unlayer.com/social/icons/rounded-black/instagram.png"
                                                                                            alt="Instagram"
                                                                                            title="Instagram" width="32"
                                                                                            style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                                                    </a>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if (mso)|(IE)]></td><![endif]-->


                                                                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                                                </div>
                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 0px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <table height="0px" align="center" border="0"
                                                                cellpadding="0" cellspacing="0" width="100%"
                                                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #000000;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td
                                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                            <span>&nbsp;</span>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td class="v-container-padding-padding"
                                                            style="overflow-wrap:break-word;word-break:break-word;padding:10px 60px 60px;font-family:arial,helvetica,sans-serif;"
                                                            align="left">

                                                            <div class="v-line-height v-font-size"
                                                                style="font-size: 14px; line-height: 140%; text-align: center; word-wrap: break-word;">
                                                                <p style="font-size: 14px; line-height: 140%;">We are
                                                                    GrabWebHost, a web hosting company with 24/7
                                                                    customer support. We provide best hosting solutions
                                                                    for your hosting needs. Our clients from personal to
                                                                    corporate. Our data center are all over the world to
                                                                    ensure your website is always up. You can choose
                                                                    shared hosting, vps hosting or cloud hosting. You
                                                                    can also be hosting reseller here. Happy hosting
                                                                    with us.</p>
                                                                <p style="font-size: 14px; line-height: 140%;">&nbsp;
                                                                </p>

                                                            </div>

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div><!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>



                    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                </td>
            </tr>
        </tbody>
    </table>
    <!--[if mso]></div><![endif]-->
    <!--[if IE]></div><![endif]-->



</body>

</html> ''', subtype='html')


with smtplib.SMTP_SSL('mail.grabwebhost.in', 465) as smtp:
    smtp.login('marketing@grabwebhost.in', 'ZW00Me)BA,MX') 
    smtp.send_message(msg)
f1=open('C:\\Users\\sajid ali\\OneDrive\\Desktop\\output.txt','w')
f1.seek(0)
f1.truncate()
f1.writelines(data[29:])
f1.close()
 
