

/*
 * GLOBAL VARIABLES
 */
//GENERATE LOGIC SLOTS
var slotmatrix = [];
for (i = 0; i <5; i++){
  slotmatrix.push([])
  for(j = 0; j<18; j++){
    slotmatrix[i].push(0);
  }
}


function create_selectable_slots(){
    var slots = document.getElementById('gridlist0');
    var boxHeight = slots.offsetHeight;
    var slotHeight = boxHeight/19;
    var slotWidth = slots.offsetWidth;
    //GENERATE SELECTABLE SLOTS
    for (i = 0; i <5; i++){
      var dia = document.getElementById("gridlist"+i)
      for(j = 0; j<18; j++){
        var listNode = document.createElement("LI")
        var listDiv = document.createElement("div")
        listDiv.classList.add("selectable_slot")
        listDiv.setAttribute("id", "slot"+i+"_"+j)
        listDiv.style.width = slotWidth+"px";
        listDiv.style.height = slotHeight+"px";
        listDiv.addEventListener("click",clickSlot)
        listNode.appendChild(listDiv)
        dia.appendChild(listNode)

      }
    }
    //slots.appendChild(document.createElement("LI").appendChild(document.createTextNode("holis")))

}

function clickSlot(element){
  var idSlot = element.explicitOriginalTarget.id;
  var newi = idSlot[4];
  var newj = idSlot.substr(6);
  var slotDiv = document.getElementById(idSlot);

  if (slotmatrix[newi][newj] == 1) {
    slotDiv.style.backgroundColor = null;
    slotmatrix[newi][newj] = 0;
  } else {
    slotDiv.style.backgroundColor = "rgba(49, 116, 224, 0.5)";
    slotmatrix[newi][newj] = 1;
  }
}


create_selectable_slots()
