describe('Home Page', function() {
    it('Open Home Page', function () {
        cy.visit('http://localhost:8080/')             //URL muss noch geändert werden
        cy.get('button').click()
    })
})
