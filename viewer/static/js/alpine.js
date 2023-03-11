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
        },
        toggleColumnButton() {
            this.columnButton = ! this.columnButton
        }
    })
})