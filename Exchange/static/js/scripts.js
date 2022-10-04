//document.getElementById("reverse_button").onclick = function () {
//    var select_from = document.getElementById("from_curr");
//    var value_from = select_from.value;
//    var select_to = document.getElementById("to_curr");
//    var value_to = select_to.value;
//    select_from.set
//    select_to
//}

//function swapBySelectedIndex(#from_curr, #to_curr) {
//  // get both elements and save the selectedIndex of the first element
//  var elem1 = document.querySelector("#from_curr"),
//      elem2 = document.querySelector("#to_curr"),
//      selectedOption1 = elem1.selectedIndex;
//
//  // set the first element to the second elements selectedIndex
//  elem1.selectedIndex = elem2.selectedIndex;
//  // set the second elements' selectedIndex to the saved index
//  elem2.selectedIndex = selectedOption1;
//}

//function getSelectedOption( elem ) {
//  return elem.options[elem.selectedIndex].value;
//}
//
//function setSelectedOption( elem, value ) {
//  for (let i = 0; i < elem.options.length; i++) {
//    elem.options[i].selected = value === elem.options[i].value;
//  }
//}
//
//function swapByOptionValue( selector1, selector2 ) {
//  var elem1 = document.querySelector(selector1),
//      elem2 = document.querySelector(selector2),
//      selectedOption1 = getSelectedOption( elem1 ),
//      selectedOption2 = getSelectedOption( elem2 );
//  setSelectedOption( elem1, selectedOption2 );
//  setSelectedOption( elem2, selectedOption1 );
//}
//
//function swapBySelectedIndex( selector1, selector2 ) {
//  var elem1 = document.querySelector(selector1),
//      elem2 = document.querySelector(selector2),
//      selectedOption1 = elem1.selectedIndex;
//
//  elem1.selectedIndex = elem2.selectedIndex;
//  elem2.selectedIndex = selectedOption1;
//}


function swapit() {
    var second=document.getElementById("to_curr");
	var first=document.getElementById("from_curr");
	var temp;
	temp=second.value;
	second.value=first.value;
	first.value=temp;
}


