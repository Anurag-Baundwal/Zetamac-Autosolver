function triggerEvent(el, type) {
    var e = new KeyboardEvent(type, {bubbles: true, cancelable: true});
    el.dispatchEvent(e);
  }
  
  var question, answer, answerField;
  answerField = document.getElementsByClassName('answer')[0];
  
  var interval = setInterval(() => {
    question = document.getElementsByClassName('problem')[0].innerText.replace('×', '*').replace('÷', '/').replace('–', '-');
    answer = eval(question);
    answerField.value = answer;
    triggerEvent(answerField, 'keydown');
  }, 0);