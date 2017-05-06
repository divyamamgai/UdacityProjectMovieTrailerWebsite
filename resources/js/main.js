(function (w, d, $) {

    // Cache the reference to the jQuery object of the elements since
    // jQuery selection operation is expensive.
    var $popUpFrame,
        $popUpContentContainer,
        // Cache the iframe element so as to speed up the append process.
        $popUpContentCache = $('<iframe frameborder="0"></iframe>');

    /**
     * Generates the YouTube URL for the provided YouTube Video ID.
     * @param {string} youTubeID
     * @returns {string}
     */
    function generateYouTubeURL(youTubeID) {
        return 'http://www.youtube.com/embed/' + youTubeID + '?autoplay=1&html5=1';
    }

    /**
     * Shows the PopUp with the trailer corresponding to the URL provided.
     * @param {string} trailerURL
     */
    function showPopUp(trailerURL) {
        if (!$popUpFrame.hasClass('show')) {
            // Append new clone of $popUpContentCache element with the source attribute
            // as the trailerURL (given in the parameter) to the $popUpContentContainer element.
            $popUpContentContainer
                .append($popUpContentCache.clone().attr('src', trailerURL));
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
                    // Clear the Popup Content before hiding so that the YouTube player
                    // stops playing to save the user's bandwidth.
                    $popUpContentContainer.empty();
                    // Removing show class of $popUpFrame element to hide it.
                    $popUpFrame.removeClass('show hiding');
                });
        }
    }

    $(function () {
        // On load cache jQuery objects of the required elements.
        $popUpFrame = $('#popup-frame', d);
        $popUpContentContainer = $('#popup-content-container', $popUpFrame);
    });

    $(d)
    // Bind the onclick event for the Close button of the $popUpFrame.
        .on('click', '#popup-frame .glyphicon-remove', hidePopUp)
        .on('click', '.movie-watch-button', function () {
            // Generate YouTube Trailer URL using the YouTube ID in
            // the data attribute of the watch button pressed.
            showPopUp(generateYouTubeURL($(this).data('trailer-youtube-id')));
        });

})(window, document, jQuery);