$(document).ready(function () {
  $(".accept-btn").on("click", function () {
    const eventId = $(this).data("event-id");
    const currentUserId = $(this).data("user-id");
    const sendId = $(this).data("send-id");

    // 1. Update the event as accepted
    $.ajax({
      url: `/api/event/${eventId}`,
      type: "PUT",
      contentType: "application/json",
      data: JSON.stringify({
        accepted: true,
        accepted_by: currentUserId,
      }),
      success: function (response) {
        // 2. Insert into calendar table
        $.ajax({
          url: "/api/calendar",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({
            send_id: sendId,
            accept_id: currentUserId,
            event_id: eventId,
          }),
          success: function (calendarResponse) {
            console.log("Event accepted and added to calendar!");
            location.reload();
          },
          error: function (xhr) {
            console.log("Calendar error: " + xhr.responseJSON.message);
          },
        });
      },
      error: function (xhr) {
        console.log("Event error: " + xhr.responseJSON.message);
      },
    });
  });
});
