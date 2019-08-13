






// Since this is still a jsp, I inlined these util functions
var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
function encode64(input)
{
   var output = "";
   var chr1, chr2, chr3;
   var enc1, enc2, enc3, enc4;
   var i = 0;

   do {
      chr1 = input.charCodeAt(i++);
      chr2 = input.charCodeAt(i++);
      chr3 = input.charCodeAt(i++);

      enc1 = chr1 >> 2;
      enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
      enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
      enc4 = chr3 & 63;

      if (isNaN(chr2))
      {
         enc3 = enc4 = 64;
      }
      else if (isNaN(chr3))
      {
         enc4 = 64;
      }

      output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + 
         keyStr.charAt(enc3) + keyStr.charAt(enc4);
   } while (i < input.length);
   
   return output;
}

function decode64(input)
{
   var output = "";
   var chr1, chr2, chr3;
   var enc1, enc2, enc3, enc4;
   var i = 0;

   // remove all characters that are not A-Z, a-z, 0-9, +, /, or =
   input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

   do
   {
      enc1 = keyStr.indexOf(input.charAt(i++));
      enc2 = keyStr.indexOf(input.charAt(i++));
      enc3 = keyStr.indexOf(input.charAt(i++));
      enc4 = keyStr.indexOf(input.charAt(i++));

      chr1 = (enc1 << 2) | (enc2 >> 4);
      chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
      chr3 = ((enc3 & 3) << 6) | enc4;

      output = output + String.fromCharCode(chr1);

      if (enc3 != 64)
      {
         output = output + String.fromCharCode(chr2);
      }
      if (enc4 != 64)
      {
         output = output + String.fromCharCode(chr3);
      }
   } while (i < input.length);

   return output;
}

function getXmlHttpRequest()
{
    // create a XMLHttpRequest object
    try
    {
        xmlHttpRequest = new XMLHttpRequest();
    }
    catch ( error )
    {
        
        xmlHttpRequest = new ActiveXObject("Microsoft.XMLHTTP");
    }

    return xmlHttpRequest;
}

function httpGet( xmlHttpRequest, url, readyStateChangeFunction )
{
    if ( readyStateChangeFunction == null )
    {
        xmlHttpRequest.open( "GET", url, false );
    }
    else
    {
        xmlHttpRequest.open( "GET", url, true );
        xmlHttpRequest.onreadystatechange = readyStateChangeFunction;
    }

    xmlHttpRequest.send(null);
}

var alertXmlHttpRequest;
var alreadyWarned = false;
function alertQueryCallback()
{
    var debugMessage;

    if (alertXmlHttpRequest.readyState == 4)
    {
        if (alertXmlHttpRequest.status == 200)
        {
            // pull out the status and the next time to check
            var xmlDocument = alertXmlHttpRequest.responseXML;
            var alertCode = xmlDocument.getElementsByTagName('statusCode').item(0).firstChild.data;
            var timeRemaining = xmlDocument.getElementsByTagName('timeRemaining').item(0).firstChild.data;
            var refreshMillis = xmlDocument.getElementsByTagName('refreshMillis').item(0).firstChild.data;
            debugMessage = "alertCode=" + alertCode + " refreshMillis=" + refreshMillis;

            if ( alertCode == 200 )                // logging out, stop polling
            {
                window.top.location.href = "https://www.my.bham.ac.uk/cp/home/logout";
            }
            else if ( alertCode == 100 )           // timing out
            {
                if ( ! alreadyWarned )
                {
                    alreadyWarned = true;
                    if ( typeof showAlertSessionExpireMessage != 'undefined' )
                    {
                         showAlertSessionExpireMessage( timeRemaining );
                    }
                }
            }
            else if ( alertCode == 50 )            // alert message
            {
                alertEncodedMessage = xmlDocument.getElementsByTagName('message').item(0).firstChild.data;
                alertMessage = decode64( alertEncodedMessage );
                debugMessage += " -- alertMessage '" + alertMessage + "'";
                if ( typeof showAlertSessionExpireMessage != 'undefined' )
                {
                    showAlertAdminMessage( alertMessage );
                }
            }
            else
            {
                alreadyWarned = false; // in case session timer is reset
            }

            if ( alertCode == 1 && refreshMillis > 0 )
            {
                debugMessage += " -- sleeping for " + refreshMillis;
	        // debug refresh millis
	        //refreshMillis = 10000;
                setTimeout( "doXmlPoll()", refreshMillis );
            }

            //window.status = debugMessage;
	    //alert( debugMessage );
        }
    }
}

function doXmlPoll()
{
    alertXmlHttpRequest = getXmlHttpRequest();
    url = /*URL*/ "https://www.my.bham.ac.uk/cp/alert/as?getAlertMessage=true";
    httpGet( alertXmlHttpRequest, url, alertQueryCallback );
}

function checkForWindowClosing()
{
    var browser=navigator.userAgent.toLowerCase();
    if ( typeof mainWindow == "boolean" &&
         mainWindow == true &&        // only main window
         (browser.indexOf("msie") != -1) &&  // only Internet Explorer
         window.event.clientX < 0 &&  // denotes that they did not click inside
         window.event.clientY < 0 )   //   the browser window
    {
        logoutXmlHttpRequest = getXmlHttpRequest();
        httpGet( logoutXmlHttpRequest, /*URL*/ "https://www.my.bham.ac.uk/cp/home/logout?src=timeout.jsp" );
    }
}

autoLogoutInternetExplorer = false;
if ( autoLogoutInternetExplorer &&
     typeof window.attachEvent != "undefined" )
{
    window.attachEvent( "onunload", checkForWindowClosing, true );
}

doXmlPoll();
