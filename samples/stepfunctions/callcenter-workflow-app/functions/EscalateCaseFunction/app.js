exports.handler = (event, context, callback) => {
    // Escalate the support case 
    var myCaseID = event.Case;
    var myCaseStatus = event.Status;
    var myMessage = event.Message + "escalating.";
    var result = { Case: myCaseID, Status: myCaseStatus, Message: myMessage };
    callback(null, result);
};