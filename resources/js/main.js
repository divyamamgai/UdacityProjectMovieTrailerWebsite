(function (w, d, $) {

    // Cache the reference to the jQuery object of the elements since
    // jQuery selection operation is expensive.
    var $popUpFrame,
        $popUpContentTrailer;

    /**
     * Shows the PopUp with the trailer corresponding to the URL provided.
     * @param {string} trailerURL
     */
    function showPopUp(trailerURL) {
        if (!$popUpFrame.hasClass('show')) {
            // Set the src of the iframe to the trailer URL.
            $popUpContentTrailer.attr('src', trailerURL);
            // Add show class to the $popUpFrame element so that it is visible.
            $popUpFrame.addClass('show');
        }
    }

    /**
     * Hides the PopUp. Called on click of Close button of the PopUp.
     */
    function hidePopUp() {
        if (!$popUpFrame.hasClass('hiding')) {
            // Animate the $popUpFrame element to fade out.
            $popUpFrame
                .addClass('hiding')
                .animate({
                    opacity: 0
                }, 500, 'swing', function () {
                    // Clear the src of the iframe inorder to save user's bandwidth.
                    $popUpContentTrailer.attr('src', '');
                    // Removing show class of $popUpFrame element to hide it.
                    $popUpFrame
                        .removeAttr('style')
                        .removeClass('show hiding');
                });
        }
    }

    $(function () {
        // On load cache jQuery objects of the required elements.
        $popUpFrame = $('#popup-frame', d);
        $popUpContentTrailer = $('#popup-content-container iframe', $popUpFrame);
    });

    $(d)
    // Bind the onclick event for the Close button of the $popUpFrame.
        .on('click', '#popup-frame .glyphicon-remove', hidePopUp)
        .on('click', '.movie-watch-button', function () {
            showPopUp($(this).data('trailer-url'));
        });

})(window, document, jQuery);