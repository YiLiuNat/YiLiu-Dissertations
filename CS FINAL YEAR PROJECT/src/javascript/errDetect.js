function errDetect(){
    try{
    	setTimeout(function(){
    		if(window.google){
    			console.log("Google Maps Loaded");
    		}else{
    			alert("Your browser does not support Google Maps API. Please try another browser!")
    		}
    	},2000)
    }catch(e){
    	alert(e);
    }
}
errDetect();
