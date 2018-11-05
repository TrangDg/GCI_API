describe('Testing GCI API', function() {
	it('Visits homepage', function() {
		cy.visit('/')

		cy.contains('GCI sample reference data')
	})
	// Testing content negotiation for 'text/html'
	it('Request "text/html" content-type', function() {
		cy
			.request({
				url: '/gci/STNN23588', 
				headers: {
					'Content-Type': 'text/html'
				}
				
			})
			.its('body').should('include', 'View JSON')
	})
	// Testing content negotiation for 'application/json'
	it('Request "application/json" content-type', function() {
		cy
			.request({
				url: '/gci/STNN23588', 
				headers: {
					'Content-Type': 'application/json'
				}
				
			})
			.its('body').should('include', '"id": "http://localhost:5000/gci/ManMadeObject/STNN23588"')
	})
	// Rendering the error page 'format_suggest.html' 
	// when requested content-type is other than 'text/html' and 'application/json'
	it('Request content-type other than html or json', function() {
		cy
			.request({
				url: '/gci/STNN23588', 
				headers: {
					'Content-Type': 'application/pdf'
				}
			})
			.its('body').should('include', 'Currently your requested content-type is not supported')

	})
	// Testing the links to ".html" and ".json" on the error page 'format_suggest.html'
	it('Return the html and json display of the requested sample', function() {
		cy.visit('/gci/STNN23588')
		cy.contains('HTML').click()
		cy.url().should('include', '/STNN23588.html')
		cy.contains('View JSON').click()
		cy.go('back')
		cy.go('back')
		cy.contains('JSON').click()
		cy.url().should('include', '/STNN23588.json')
		cy.contains('"id": "http://localhost:5000/gci/ManMadeObject/STNN23588"')
	})
	// Testing typo by user
	it('Return the 404 error page', function() {
		cy.visit('gci/WOOD10000')
		cy.contains('HTML').click()
		cy.url().should('include', 'WOOD10000.html')
		cy.contains('404 Error :(')
		cy.go('back')
		cy.contains('JSON').click()
		cy.url().should('include', '/WOOD10000.json')
		cy.contains('404 Error :(')
	})


	
})


