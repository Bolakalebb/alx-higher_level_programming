$(document).ready(function() {
  // Include item to the list when user clicks on add button
  $('#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });
  
  // Delete last item from the list when user clicks on remove button
  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });
  
  // Delete all items from the list when user clicks on clear button
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
