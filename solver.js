function triggerEvent(el, type){
    var e = document.createEvent('HTMLEvents');
    e.initEvent(type, false, true);
    el.dispatchEvent(e);
}

var question, answer, answerField;
var interval = setInterval(() => {
question = document.getElementsByClassName('problem')[0].innerText.replace('×', '*').replace('÷', '/').replace('–', '-');
answer = eval(question);
answerField = document.getElementsByClassName('answer')[0];
answerField.value = answer;
triggerEvent(answerField, 'keydown');
}, 0.00000000001);