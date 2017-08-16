$('#loginButton').click(function(){
  $('#loginForm').slideToggle('slow');
  $('#registrationForm').slideUp('slow');
})

$('#registrationButton').click(function(){
  $('#registrationForm').slideToggle('slow');
  $('#loginForm').slideUp('slow');
})
