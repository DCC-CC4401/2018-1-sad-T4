

/*
 * GLOBAL VARIABLES
 */
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
$( window ).on( "load", create_space_filter() )
