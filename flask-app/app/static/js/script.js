console.log("Hello from script.js");

// Example usage: Accept an event with a button click
$(".accept-btn").on("click", function () {
  const eventId = $(this).data("event-id");
  const currentUserId = $(this).data("user-id"); // Set this in your template

  $.ajax({
    url: `/api/event/${eventId}`, // Adjust if your blueprint uses a prefix
    type: "PUT",
    contentType: "application/json",
    data: JSON.stringify({
      accepted: true,
      accepted_by: currentUserId, // Add this field if you want to track who accepted
    }),
    success: function (response) {
      console.log("Event accepted!");
      location.reload(); // Optionally reload to update UI
    },
    error: function (xhr) {
      console.log("Error: " + xhr.responseJSON.message);
    },
  });
});
