README - Atur Aja Website

1. How to Use the Website Files (HTML, CSS, JS)
------------------------------------------------
- Open the HTML files (e.g., index.html, login.html, register.html, dashboard.html, input.html, simulasi.html, laporan.html) in a web browser to view the respective pages.
- The styles.css file contains all the styling rules for the website and is linked in the HTML files.
- The main.js file contains JavaScript code to handle interactive features and simulation logic.
- To modify the website, edit the HTML for structure/content, CSS for styling, and JS for behavior.

2. File Structure and Dependencies
-----------------------------------
- index.html          : Landing page (Beranda)
- login.html          : Login page
- register.html       : Registration page
- dashboard.html      : User dashboard showing summaries and navigation
- input.html          : Data input page for raw materials and products
- simulasi.html       : Production simulation page with input options
- laporan.html        : Reports page listing past simulation results
- styles.css          : CSS stylesheet for consistent design and responsiveness
- main.js             : JavaScript file for interactivity and simulation calculations
- README.txt          : This documentation file
- website_flow.png    : Flowchart diagram of the user journey and workflow
- website_flow.diagram_editor : Mermaid diagram source code for the flowchart
- website_flow.mmd    : Additional flowchart source file

3. Instructions for Local Testing
----------------------------------
- Ensure all files are in the same directory or maintain relative paths as provided.
- Open index.html in a modern web browser (Chrome, Firefox, Edge, Safari).
- Navigate through the website using the provided links and buttons.
- For full functionality, JavaScript must be enabled in the browser.
- No backend server is required for basic navigation and UI testing.
- To test data input and simulation features, interact with the forms on input.html and simulasi.html.
- For persistent data or advanced features, integration with a backend/database is needed (not included).

4. Notes About the Simulation Functionality
--------------------------------------------
- The simulation allows users to input either a target profit or available raw materials.
- Based on inputs, the system calculates:
  * Estimated product quantities to produce
  * Total production cost and potential revenue
  * Remaining raw materials after production
  * Recommendations for the most profitable products
- Simulation results can be saved and viewed later in the Laporan (Reports) section.
- The current implementation simulates calculations on the client side using JavaScript.
- For real-world use, backend integration and data persistence should be implemented.

5. Deployment Instructions for Public Access
---------------------------------------------
This website is a static site that uses client-side JavaScript and localStorage for data persistence, so no backend server is required. You can deploy it easily on various static hosting platforms:

**A. Deploying with GitHub Pages**
1. Create a GitHub repository and push all website files to the repository.
2. In the repository settings, go to the "Pages" section.
3. Select the branch (usually `main` or `master`) and the root folder (or `/docs` if you use that).
4. Save the settings and wait a few minutes.
5. Your website will be available at `https://<your-username>.github.io/<repository-name>/`.
6. You can configure a custom domain in the GitHub Pages settings if desired.

**B. Deploying with Netlify**
1. Create a free account on Netlify (https://www.netlify.com/).
2. Connect your GitHub repository or drag and drop your website folder in the Netlify dashboard.
3. Netlify will automatically build and deploy your site.
4. Your site will be available at a Netlify subdomain (e.g., `https://your-site.netlify.app`).
5. You can add a custom domain and enable free SSL certificates via Netlify settings.

**C. Deploying on Traditional Web Hosting**
1. Upload all website files to your web hosting server via FTP or file manager.
2. Ensure the files maintain their relative paths.
3. Access your website via your hosting domain.
4. Make sure your hosting supports serving static files and has SSL enabled for HTTPS.

**Notes:**
- Since the website uses localStorage, user data is stored locally in the browser and will not sync across devices or users.
- For a professional public deployment, consider configuring a custom domain and enabling HTTPS/SSL certificates to secure your site.
- Services like GitHub Pages and Netlify provide free SSL certificates automatically.
- If you want multi-user support or centralized data storage, backend development and database integration will be necessary.

6. Contact Information for Support
-----------------------------------
- For questions, issues, or feature requests, please contact:
  Email: support@aturaja.com
  Phone: +62 812 3456 7890
  Website: https://www.aturaja.com/contact

Thank you for using Atur Aja!