# How to run the programme
*Yi Liu - March 2019*

### Pre-requisites:

1. An Internet connection.
2. A computer or smart phone with any modern browser (Google Chrome is recommended).
3. Make sure (1) the private mode of your web browser is turned off and (2) the location service
    is turned on.

### Run:

Open “/src/html/index.htm” or visit https://yiliunat.github.io/fyp on your browser.

### Test Scheme:

1. **Basic functions:**
    1.1 Click the drop-down menu and select any building to test the navigation function.
    1.2 To test the multiple entrance function, select any building mentioned in Note (II).
    1.3 Experiment with the different facility buttons by clicking them.
2. **Timetable Upload:**
    2.1 Open the sidebar (the top-left button), click “ _upload your timetable_ ” button, select one
       of the my.bham timetable samples in “ _/src/timetable_samples/_ ” and upload the file
       named “ _upload_this_file.html_ ” (this is the same as the “ _timeout.html_ ” file in the
       “ _visualized timetable_ ” folder).
    2.2 “ _Visualized timetable_ ” is the my.bham timetable with their style sheets. If you want to
       check the correctness of the loaded timetable, you can open “ _timeout.html_ ” in any
       “ _visualized timetable_ ” folder.
    2.3 Once you upload the timetable, you can refresh the page or close the browser, the
       uploaded timetable will be automatically loaded the next time you use the programme.
3. **Check the correctness of the timetable parsing:**
    3.1 The uploaded timetable will be loaded in the sidebar (the top-left button).
4. **Check the correctness of the lecture reminder:**
    4.1 Open the test panel (the top-right calendar button). Change the system time to see
       how the lecture reminder outputs differs.
5. **Delete the uploaded timetable:**
    5.1 Open the sidebar (the top-left button) and click the “ _delete this timetable_ ” button.

### Note:
(I) Not all the coordinates of UoB buildings were recorded in this system, such an
implementation would be very time consuming and irrelevant to the computer science field.

(II) The following buildings are samples of multiple entrance building:
[ _‘Aston Webb Great Hall’, ‘Staff House’, ‘Library’_ ]



