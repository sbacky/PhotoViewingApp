// viewer/static/js/alpine.js

document.addEventListener('alpine:init', () => {
    Alpine.store('buttons', {
        init() {
            this.listButton = true,
            this.columnButton = false
        },

        listButton: true,
        columnButton: false,

        toggleListButton() {
            this.listButton = ! this.listButton
            if (this.listButton) {
                window.console.log("Button is-selected");
            } else {
                window.console.log("Button un-selected");
            }
        },
        toggleColumnButton() {
            this.columnButton = ! this.columnButton
            if (this.columnButton) {
                window.console.log("Button is-selected");
            } else {
                window.console.log("Button un-selected");
            }
        }
    })
})