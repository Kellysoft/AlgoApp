$('.questionText').click(function(){
  $('.questionHintButton').slideToggle('slow');
})

$('.questionNfoButton').click(function(){
  $('.questionNfo').slideToggle('slow');
})

$('.questionHintButton').click(function(){
  $('.questionHint').slideToggle('slow');
})

$('.userInputSubmit').click(function(){
  $('.algoConsole').slideToggle('slow');
})

$('.questionSolutionButtonOne').click(function(){
  $('.questionSolutionOne').slideToggle('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionHint').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionSolutionButtonTwo').click(function(){
  $('.questionSolutionTwo').slideToggle('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionHint').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionExplanationButton').click(function(){
  $('.questionExplanation').slideToggle('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionHint').slideUp('slow');
})
