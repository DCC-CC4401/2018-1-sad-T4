

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

function createReservations(){

  var space_reservations = [];
  var block_reservations = [];

  for (i = 0; i <5; i++){
    var bini = null;
    var blen = null;

    var started_res = false;
    for(j = 0; j<18; j++){

      if (slotmatrix[i][j] == 0 || j == 17) {
        if(started_res){
          started_res = false;
          blen = j == 17 ? blen+1 : blen;
          block_reservations.push({d:i, ini:bini, len:blen});
        } else {
          if (j==17 && slotmatrix[i][j] == 1) {block_reservations.push({d:i, ini:j, len:1});}
          continue;
        }
      } else {
        if(started_res){
          blen += 1;
        } else {
          bini = j;
          blen = 1;
          started_res = true;


        }
      }

    }
    started_res = false;
  }


  for(index in block_reservations){
    var res = block_reservations[index];
    var weekday = getMonday();
    weekday.setDate( weekday.getDate() + res.d)

    weekday.setHours(9)
    weekday.setMinutes(0)
    weekday.setSeconds(0);weekday.setMilliseconds(0);
    //fecha inicio:
    weekday.setTime(weekday.getTime() + 1000*60*30*res.ini)
    dt_inicio = convertUTCDateToLocalDate(new Date(weekday.getTime())).toISOString().substr(0,16)
    dt_inicio = dt_inicio.substr(0,10)+" "+dt_inicio.substr(11)
    //fecha termino:
    weekday.setTime(weekday.getTime() + 1000*60*30*res.len)
    dt_fin = convertUTCDateToLocalDate(new Date(weekday.getTime())).toISOString().substr(0,16)
    dt_fin = dt_fin.substr(0,10)+" "+dt_fin.substr(11)

    space_reservations.push({dti:dt_inicio, dtf:dt_fin})
    document.getElementById("toReserve").setAttribute("value", JSON.stringify(space_reservations))
  }


  console.log(space_reservations)
}

function getMonday() {
  d = new Date();
  var day = d.getDay(),
      diff = d.getDate() - day + (day == 0 ? -6 : 1);
  return new Date(d.setDate(diff));
}
function convertUTCDateToLocalDate(date) {
    var newDate = new Date(date.getTime()+date.getTimezoneOffset()*60*1000);

    var offset = date.getTimezoneOffset() / 60;
    var hours = date.getHours();

    newDate.setHours(hours - offset);

    return newDate;
}

create_selectable_slots()
