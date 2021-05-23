if(document.getElementById("toggle-comment-form")) {
  const commentFormToggleButton = document.getElementById("toggle-comment-form");
  const commentFormContainer = document.getElementById("add-comment__container");
  const nameInput = document.getElementById("form1__name");
  const emailInput = document.getElementById("form1__email");
  const commentInput = document.getElementById("form1__comment");
  const btnInput = document.getElementById("form1__btn");
  
  commentFormToggleButton.addEventListener('click', togglecommentForm); 
  commentFormToggleButton.innerHTML = "Add Comment"

  // Disable form input focus when page is first loaded (form is closed)
  nameInput.tabIndex=-1
  emailInput.tabIndex=-1
  commentInput.tabIndex=-1 
  btnInput.tabIndex=-1    
  
  function togglecommentForm() {
    commentFormToggleButton.blur();
    commentFormContainer.classList.toggle("add-comment__container--visible");
    var initial = setTimeout(toggle, 0);
    function toggle() {
      clearTimeout(initial);
      if(commentFormToggleButton.innerHTML == "Add Comment") {
        commentFormToggleButton.innerHTML = "Close Comment Form"
        // Enable form input focus (form is open) 
        nameInput.tabIndex=0
        emailInput.tabIndex=0
        commentInput.tabIndex=0 
        btnInput.tabIndex=0   
      }
      else {
        commentFormToggleButton.innerHTML = "Add Comment"
        // Disable form input focus (form is closed) 
        nameInput.tabIndex=-1
        emailInput.tabIndex=-1
        commentInput.tabIndex=-1 
        btnInput.tabIndex=-1                   
      }
    }
  }
}
