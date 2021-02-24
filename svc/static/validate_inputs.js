var inputs = document.getElementsByTagName("input");
var help = document.getElementById("help");
function validate(event){
  for (let i=0;i<inputs.length;i++){
    if(inputs[i].value.indexOf("script")>-1 || inputs[i].value.indexOf("<")>-1){
      disable();
      help.innerHTML = "<b class='text-secondary'>Use the fields as they should be...........</b>"
      break;
    } else {
      enable();
      help.innerHTML = ""
    }
  }
}
for (let i=0;i<inputs.length;i++){
  inputs[i].setAttribute('oninput', 'validate(event)');
}

function disable(){
  console.log("hua")
  var submitBtn = document.getElementById('submitBtn');
  submitBtn.setAttribute('disabled', 'true');
}
function enable(){
  console.log("hua")
  var submitBtn = document.getElementById('submitBtn');
  submitBtn.removeAttribute('disabled');
}
