// $('.questionText').click(function(){
//   $('.algoConsole').slideToggle('slow');
// })

$('.questionNfoButton').click(function(){
  $('.questionNfo').slideToggle('slow');
  $('.questionHint').slideUp('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionHintButton').click(function(){
  $('.questionHint').slideToggle('slow');
  $('.questionNfo').slideUp('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionSolutionButtonOne').click(function(){
  $('.questionSolutionOne').slideToggle('slow');
  $('.questionNfo').slideUp('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionHint').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionSolutionButtonTwo').click(function(){
  $('.questionSolutionTwo').slideToggle('slow');
  $('.questionNfo').slideUp('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionHint').slideUp('slow');
  $('.questionExplanation').slideUp('slow');
})

$('.questionExplanationButton').click(function(){
  $('.questionExplanation').slideToggle('slow');
  $('.questionNfo').slideUp('slow');
  $('.questionSolutionOne').slideUp('slow');
  $('.questionSolutionTwo').slideUp('slow');
  $('.questionHint').slideUp('slow');
})
