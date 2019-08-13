  var agt=navigator.userAgent.toLowerCase();
  
  var is_major = parseInt(navigator.appVersion);
  
  var is_minor = parseFloat(navigator.appVersion); 
  
  var is_moz = false;
  var is_fox = false;
  var is_saf = false;
  var is_nav      = ((agt.indexOf('mozilla')!=-1) && (agt.indexOf('spoofer')==-1) 
                     && (agt.indexOf('compatible') == -1) && (agt.indexOf('opera')==-1) 
                     && (agt.indexOf('webtv')==-1)); 
  var is_nav2     = (is_nav && (is_major == 2)); 
  var is_nav3     = (is_nav && (is_major == 3)); 
  var is_nav4     = (is_nav && (is_major == 4)); 
  var is_nav4up   = (is_nav && (is_major >= 4)); 
  var is_nav4_7up = (is_nav && ((is_minor >= 4.7) && (is_major != 5)));
  var is_navonly  = (is_nav && ((agt.indexOf(";nav") != -1) || (agt.indexOf("; nav") != -1)) ); 
  var is_nav5     = (is_nav && (is_major == 5));
  if (is_nav5 || agt.indexOf("rv:1.7.12") != -1 || agt.indexOf("rv:1.8") != -1)
  { 
      var undefined;
      var version;
      if ( agt.indexOf("netscape") == -1 && agt.indexOf("firefox") == -1 )
      {
          is_moz = true;
          version = agt.split("rv:");
      }
      if ( agt.indexOf("firefox") != -1 )
      {
          is_fox = true;
          version = agt.split("firefox/");
      }
      if ( agt.indexOf("safari") != -1 )
      {
          is_saf = true;
          version = agt.split("applewebkit/");
      }
      if ( agt.indexOf("netscape6/") != -1 )
      {
          version = agt.split("netscape6/"); 
      }
      if ( agt.indexOf("netscape/7") != -1 )
      {
          version = agt.split("netscape/");
      }
      if ( agt.indexOf("netscape/8") != -1 )
      {
          version = agt.split("netscape/");
      }
      if (version != undefined)
      {
          is_major = parseInt(version[1].slice(0,1));
          is_minor = parseFloat(version[1].slice(0,3));
      }
  }
  var is_nav6     = (is_nav && (is_major == 6));
  var is_nav6up   = (is_nav && (is_minor >= 6));
  var is_nav6_2up = (is_nav && (is_minor >= 6.2) && (is_major != 7));
  var is_nav7     = (is_nav && (is_major == 7));
  var is_nav8     = (is_nav && (is_major == 8));
  var is_moz1_5   = (is_moz && (is_minor == 1.5));
  var is_moz1_6   = (is_moz && (is_minor == 1.6));
  var is_moz1_7   = (is_moz && (is_minor == 1.7));
  var is_fox1     = (is_fox && (is_major == 1));
  var is_fox1_5   = (is_fox1 && (is_minor == 1.5));
  var is_fox2_0   = (is_fox && (is_minor == 2.0));
  var is_fox3_0   = (is_fox && (is_minor == 3.0));
  var is_saf1_1   = (is_saf && is_minor >= 103);
  var is_saf1_2   = (is_saf && is_minor >= 125);
  var is_saf1_3   = (is_saf && is_minor >= 312);
  var is_saf2_0   = (is_saf && is_minor >= 412);
  var is_gecko    = (agt.indexOf('gecko') != -1);
  var is_ie     = (agt.indexOf("msie") != -1); 
  var is_ie3    = (is_ie && (is_major < 4)); 
  var is_ie4    = (is_ie && (is_major == 4) && (agt.indexOf("msie 5.0")==-1) ); 
  var is_ie4up  = (is_ie  && (is_major >= 4));
  if (is_ie4up)
  {
      var version = navigator.appVersion;
      version = version.split(";");
      is_major = parseInt(version[1].slice(5,7));
      is_minor = parseFloat(version[1].slice(5));
  }
  var is_ie5       = (is_ie && (is_major == 5));
  var is_ie5up     = (is_ie && (is_minor >= 5));
  var is_ie5upMac  = (is_ie && ((is_minor >= 5) && (is_minor <= 5.2)));
  var is_ie51upMac  = (is_ie && (is_major == 5) &&
                      (agt.indexOf("msie 5.") != -1) && 
                      (agt.indexOf("msie 5.0") == -1));
  var is_ie5_5up   = (is_ie && ((is_minor >= 5.5) || (is_major > 5)));
  var is_ie6       = (is_ie && (is_major == 6));
  var is_ie7       = (is_ie && (is_major == 7));
  var is_js; 
  if (is_nav2 || is_ie3) is_js = 1.0; 
  else if (is_nav3) is_js = 1.1; 
  else if ((is_nav4 && (is_minor <= 4.05)) || is_ie4) is_js = 1.2; 
  else if ((is_nav4 && (is_minor > 4.05)) || is_ie5) is_js = 1.3; 
  else if (is_nav5) is_js = 1.4; 
  else if (is_nav && (is_major > 5)) is_js = 1.4; 
  else if (is_ie && (is_major > 5)) is_js = 1.3; 
  else is_js = 0.0; 
  var is_win   = ( (agt.indexOf("win")!=-1) || (agt.indexOf("16bit")!=-1) );
  var is_mac    = (agt.indexOf("mac")!=-1);
  var is_macppc = (is_mac && ((agt.indexOf("ppc")!=-1) || 
                                (agt.indexOf("powerpc")!=-1)));
  var is_macosx = (is_mac && (agt.indexOf("os x")!=-1));
  var is_640x480 = false;
  var is_800x600 = false;
  var is_1024x768 = false;
  if ( is_nav4up || is_ie4up )
  {
      if ( screen.width==640 && screen.height==480 )
          is_640x480 = true;
      else if ( screen.width==800 && screen.height==600 )
          is_800x600 = true;
      else if ( screen.width==1024 && screen.height==768 )
          is_1024x768 = true;
  }
