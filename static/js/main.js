/* Add event handler for new form submission */

$(document).on('submit', '#newPlagiarismForm', function(event) {
  event.preventDefault();
  var formData = $(this).serialize();

  $.ajax({
    url: '/check_plagiarism',
    type: 'POST',
    data: formData,
    success: function(response) {
      // Display the result
      $('#plagiarismResult').text(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
});