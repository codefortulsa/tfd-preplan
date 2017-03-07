function onKeyDownFilter(event, re, next, spaceAllowedFor) {
    var keyCode = event.keyCode ? event.keyCode : event.which;
    switch (keyCode) {
        case 8:  // Backspace
        case 9:  // Tab
        case 13: // Enter
        case 37: // Left
        case 38: // Up
        case 39: // Right
        case 40: // Down
            break;
        case 32: // Space
            if(spaceAllowedFor) {
                var currentInput = $(spaceAllowedFor).val();

                if(currentInput.substr(currentInput.length - 1) !== ' ') {
                    return true;
                }
            }

            $(next).focus();
            event.preventDefault();
            return false;

            break;
        default:
            var regex = new RegExp(re);
            var key = event.key;
            if (!regex.test(key)) {
                event.preventDefault();
                return false;
            }
            break;
    }
}

$().ready(function() {
// validate signup form on keyup and submit
    $('#id_street_no').on('keydown', function (event) {
        onKeyDownFilter(event, "^[0-9]+$", "#id_street_dir", false);
    });

    $('#id_street_dir').on('keydown', function (event) {
        onKeyDownFilter(event, "^[NORnorSUuTHthEAeaWwSTst]+$", "#id_street_name", false);
    });

    $('#id_street_name').on('keydown', function (event) {
        onKeyDownFilter(event, "^[0-9a-zA-Z &\,\.\']+$", "#id_street_type", "#id_street_name");
    });

    $('#id_street_type').on('keydown', function (event) {
        onKeyDownFilter(event, "^[0-9a-zA-Z]+$", "#id_street_nbr", false);
    });
});