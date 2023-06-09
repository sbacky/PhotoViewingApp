// This is the scss entry file
import "../styles/index.scss";

// We can import Bootstrap JS instead of the CDN link, if you do not use
// Bootstrap, please feel free to remove it.
// import "bootstrap/dist/js/bootstrap.bundle";

// Import HTMX
import 'htmx.org';

window.htmx = require('htmx.org');

// Import AlpineJS
import Alpine from 'alpinejs';

window.Alpine = Alpine;

Alpine.start();

// Import fontawesome-free
import '@fortawesome/fontawesome-free/js/all';

// We can import other JS file as we like
import "../components/sidebar";
import "../../../static/js/alpine";

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
