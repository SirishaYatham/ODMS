 // Add event listener when the page loads
 document.addEventListener('DOMContentLoaded', function () {
    // Search for donors when the page loads
    searchOrgan();
});
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Function to search for donors
function searchOrgan() {
    const organInput = document.getElementById("organInput").value.trim().toLowerCase();
    
    fetch(`/get_donors/?organ=${organInput}`)
    .then(response => response.json())
    .then(donors => {
        displayDonors(donors);
    })
    .catch(error => console.error('Error:', error));
}

// Function to display donors
function displayDonors(donors) {
    const donorListContainer = document.getElementById("donor-list");
    donorListContainer.innerHTML = "";
    donors.forEach(donor => {
        const donorInfo = document.createElement("div");
        donorInfo.innerHTML = `
             <div style="border:solid black 2px;border-radius:10px;width:400px;
            margin:0px 0px 20px 0px;padding:10px 0px 10px 20px;
            background-image:linear-gradient(60deg,#005A9C,black);
"
            >
                <p>Name: ${donor.donorname}</p>
                <p>Location: ${donor.location}</p>
                <p>Age: ${donor.age}</p>
                <p>Phone Number: ${donor.contact}</p>
                <p>Organ avail: ${donor.organ}</p>
                <p>Hospital: ${donor.hospital}</p>
                <p>Blood Group: ${donor.bloodgroup}</p>
                <div class="icon-container">
                    <button class = "container-btn" onclick="deleteDonor(${donor.id})"><i class="fa fa-times" style="color:white" aria-hidden="true"></i></button>
                    <button class = "container-btn" onclick = "editDonor(${donor.id})"><i class="fa fa-pencil" style="color:white" aria-hidden="true"></i></button>
                </div>
            </div>
        `;
        donorListContainer.appendChild(donorInfo);
    });
} 


function deleteDonor(donorId) {
    window.location.href = `/receiver_details/${donorId}/`;
}

function editDonor(donorId) {
    window.location.href = `/edit_organ_donation/${donorId}/`;
}
