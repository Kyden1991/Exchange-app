document.getElementById("reverse_button").onclick = function swapit() {
debugger;
    var first=document.getElementById("from_curr");
    var second=document.getElementById("to_curr");
	var temp;
	temp=second.value;
	second.value=first.value;
	first.value=temp;
}


