

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
var selected_filter = {}
var nombres = {}


function create_space_filter(){
   var f = document.getElementsByClassName("SpcSelectListElement");

   for (index in f){
     var child = f[index].children[0].id
     var ch_id = child[1]
     var ch_name = f[index].innerText
     $('#'+child).on("click",clickFilter)
     nombres[child] = ch_name;


   }
}

function clickFilter(element){
  if(element.currentTarget.nodeName=="I"){
    if(element.currentTarget.className=="fas fa-circle"){
      delete selected_filter[element.currentTarget.id]
      element.currentTarget.className = "far fa-circle"
    } else {
        selected_filter[element.currentTarget.id] = nombres[element.currentTarget.id]
        element.currentTarget.className = "fas fa-circle"
    }
  }

  var allNodes = document.querySelectorAll('[sname]')
  if(isEmpty(selected_filter)){
    for(i = 0; i<allNodes.length; i++){
    allNodes[i].style.display = null;
    }
  } else {
    for(i = 0; i<allNodes.length; i++){
      hide = true;
      var space_name = allNodes[i].attributes.sname.nodeValue
      for(j in selected_filter){
        if (selected_filter[j]==space_name) {
          hide = false
        }
      }
      allNodes[i].style.display = hide ? "none" : null;
      hide = true;
    }

  }
  
}

function create_selectable_slots(){
    var slots = document.getElementById('gridlist0');
    var boxHeight = slots.offsetHeight;
    var slotHeight = boxHeight/19;
    var slotWidth = slots.offsetWidth;
    //GENERATE SELECTABLE SLOTS
    for (i = 0; i <5; i++){
      var day = document.getElementById("gridlist"+i)
      for(j = 0; j<18; j++){
        var listNode = document.createElement("LI")
        var listDiv = document.createElement("div")
        listDiv.classList.add("selectable_slot")
        var newId = "slot"+i+"_"+j
        listDiv.setAttribute("id", newId)
        listDiv.style.width = slotWidth+"px";
        listDiv.style.height = slotHeight+"px";
        //listDiv.addEventListener("click",clickSlot)

        listNode.appendChild(listDiv)
        day.appendChild(listNode)
        $('#'+newId).on("click",clickSlot)

      }
   }
}

function clickSlot(element){

  var idSlot = element.currentTarget.id;

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
          if (j==17 && slotmatrix[i][j] == 1) {
            block_reservations.push({d:i, ini:j, len:1});
            }
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
    var act_m = actual_monday.split("/")
    var weekday = new Date(act_m[1]+"/"+act_m[0]+"/"+act_m[2])
    //Conversion a un formato entendible por el modelo:
    weekday.setDate( weekday.getDate() + res.d)
    weekday.setHours(9);weekday.setMinutes(0);
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
}


//AUXILIARY FUNCTIONS
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
function isEmpty( obj ) {
  for ( var prop in obj ) {
    return false;
  }
  return true;
}


//'MAIN'
$( window ).on( "load", create_selectable_slots() )
$( window ).on( "load", create_space_filter() )
