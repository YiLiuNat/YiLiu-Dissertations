function isValidStringForURL(s)
{
    var invalidChars = new Array( ",", ";", "<", ">", ".", "\"", "'", "#", "\\", "/", "&", "?", "~", "!", "@", "$", "%", "^", "*", "(", ")", "+", "{", "}", "|" );
    for (var i=0;i<invalidChars.length;i++)
    {
        if (s.indexOf(invalidChars[i]) >= 0)
            return false;
    }
    return true;
}
function getInvalidCharsDisplayString()
{
    var s = ", ; < > . \" ' # \\ / & ? ~ ! @ $ % ^ * ( ) + { } or |";
    return s;
}
function setCookie(name, value) {
  var curCookie = name + "=" + escape(value) +
                  "; path=/";
  document.cookie = curCookie;
}
function getCookie(name) {
  var dc = document.cookie;
  var prefix = name + "=";
  var begin = dc.indexOf("; " + prefix);
  if (begin == -1) {
    begin = dc.indexOf(prefix);
    if (begin != 0) return null;
  } else
    begin += 2;
  var end = document.cookie.indexOf(";", begin);
  if (end == -1)
    end = dc.length;
  return unescape(dc.substring(begin + prefix.length, end));
}
function initSession()
{
  setSession();
}
function setSession() {
  var sctSession = getCookie("sctSession");
  if (sctSession == null || sctSession == "") {
    sctSession = 1;
  }
  else
  {
    ++sctSession
  }
  setCookie("sctSession", sctSession);
  setTimeout('setSession()', 3000);
}
var lastHit;
var testCount = 0;
var xWindow;
function checkSession(which)
{
  xWindow = which;
  lastHit = getCookie("sctSession");
  setTimeout('testCookie()', 2000);
}
function testCookie() {
  var sctSession = getCookie("sctSession");
  if (sctSession != null || sctSession != "") 
  {
    sctSession = parseInt(sctSession);
    lastHit = parseInt(lastHit);
    if (sctSession == lastHit && testCount <= 15)
    {
      ++testCount
      setTimeout('testCookie()', 2000);
    }
    else if (lastHit < sctSession && testCount <= 15)
    {
      testCount = 0;
      lastHit = sctSession;
      setTimeout('testCookie()', 2000);
    }
    else
    {
      deleteCookie();
      closeWindow();
    }
  }
  else
  {
    closeWindow();
  }
}
function closeWindow()
{
    if (xWindow == "cal")
    {
        stats="";
        calendarWindow = window.open ("https://www.my.bham.ac.uk/misc/windowcloser.html","calendarWindow",stats);
    }
    else
    {
        parent.parent.location.href="https://www.my.bham.ac.uk/misc/windowcloser.html";
    }
}
