/* Add event handler for new form submission */

$(document).on('submit', '#newPlagiarismForm', function(event) {
  event.preventDefault();
  var formData = $(this).serialize();

  $.ajax({
    url: '/check_plagiarism',
    type: 'POST',
    data: formData,
    dataType: 'json',
    success: function(response) {
      // Display the results
      $('#plagiarismResult').text(response.result);
    },
    error: function(xhr, status, error) {
      console.log('Error:', error);
    }
  });
});

/* Add event handler for new form submission */

$(document).on('submit', '#newJaccardForm', function(event) {
  event.preventDefault();
  var formData = $(this).serialize();

  $.ajax({
    url: '/check_jaccard',
    type: 'POST',
    data: formData,
    dataType: 'json',
    success: function(response) {
      // Display the results
      $('#jaccardResult').text(response.result);
    },
    error: function(xhr, status, error) {
      console.log('Error:', error);
    }
  });
});