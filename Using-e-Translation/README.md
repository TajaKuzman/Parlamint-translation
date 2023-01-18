Instructions:
- It is more efficient to submit a single, large document than hundreds or thousands of individual sentences. Consider submitting requests as a consolidated document.
- Plain txt format avoids conversion steps, so is slightly quicker.
-  If you submit five for English into Italian and five for English into German, they will be processed in separate streams. In the second case, the 10 translations would arrive in half the time.
-  The client needs to expose a callback URL which will receive a notification that the translation job in question has been completed. eTranslation sends the completed translation to the destination URL specified by the Client.

The following steps illustrate this interaction:
- The client sends a translation request to the eTranslation web service ;
- eTranslation web service replies synchronously with the eTranslation request ID (positive number) or an error code (negative number) ;
- eTranslation web service translates the text or document for all requested target languages ;
- Each translated text or document is sent back to the target location and the client can be notified separately for each target language via the callback URL.

- text-to-translate: the text to translate (maximum: 5000 characters).
- document-to-translate-path: the FTP or SFTP path of the document to translate
Example: ftp://user:password@ftp_server_name:21/mypath/myfile.doc
- document-to-translate-base64: contains two mandatory and one optional tag which are described below:
	- content: base 64 content
	- format: format of the document. Accepted format are odt, ods,odp,odg, ott, ots, otp, otg, rtf, doc, docx, xls, xlsx, ppt, pptx, pdf, txt, htm, html, xhtml, xml, xlf, xliff, sdlxliff, tmx, rdf
	- file-name (optional): file name of the translated document without extension. It will be suffix by an underscore and target language ISO code in uppercase - dot - chosen output format.

Any client is able to submit up to the following at the same time:
- 250 documents (1.250.000 characters)
- 500 text snippets

When these limits are exceeded, requests will be rejected with a -20028 error (Concurrency quota exceeded). Requests will continue to be rejected until the number of submissions from the client in question drops below the upper limit.