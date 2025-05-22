console.log("Hello from script.js");

$(".accept-btn").on("click", function () {
  const eventId = $(this).data("event-id");
  const currentUserId = $(this).data("user-id");

  $.ajax({
    url: `/api/event/${eventId}`,
    type: "PUT",
    contentType: "application/json",
    data: JSON.stringify({
      accepted: true,
      accepted_by: currentUserId,
    }),
    success: function (response) {
      console.log("Event accepted!");
      location.reload();
    },
    error: function (xhr) {
      console.log("Error: " + xhr.responseJSON.message);
    },
  });
});
