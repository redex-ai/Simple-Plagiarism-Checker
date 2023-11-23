/* Add or update JavaScript code to handle the new form submission via AJAX */

$(document).ready(function() {
  // Function to handle form submission
  function submitForm() {
    // Log event
    console.log('Form submitted');

    // Get form data
    var formData = {
      query: $('#query').val()
    };

    // Send AJAX request
    $.ajax({
      url: '/',
      type: 'POST',
      data: formData,
      success: function(response) {
        // Log server response
        console.log('Server response:', response);

        // Display result
        $('#output').text(response.output);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        // Log error
        console.error('AJAX error:', errorThrown);

        // Display error message
        $('#output').text('An error occurred. Please try again.');
      }
    });
  }

  // Event listener for form submission
  $('#plagiarismForm').submit(function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Log event
    console.log('Form submit event');

    // Call submitForm function
    submitForm();
  });
});