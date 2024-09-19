
function searchOrgan() {
    const organInput = document.getElementById("organInput").value.trim().toLowerCase();
    
    fetch(`/get_donors/?organ=${organInput}`)
    .then(response => response.json())
    .then(donors => {
        console.log(donors); // Add this line to debug

        displayDonors(donors);
    })
    .catch(error => console.error('Error:', error));
}

function displayDonors(donors) {
    const donorListContainer = document.getElementById("donor-list");
    donorListContainer.innerHTML = "";
    donors.forEach(donor => {
        const donorInfo = document.createElement("div");
        donorInfo.innerHTML = `
            <div style="border:solid black 2px;border-radius:10px;width:400px;
            margin:0px 0px 20px 0px;padding:10px 0px 10px 20px;
            background-image:linear-gradient(60deg,#005A9C,black);"
            >
                <p>Name: ${donor.donorname}</p>
                <p>Location: ${donor.location}</p>
                <p>Age: ${donor.age}</p>
                <p>Phone Number: ${donor.contact}</p>
                <p>Organ avail: ${donor.organ}</p>
                <p>Hospital: ${donor.hospital}</p>
                <p>Blood Group: ${donor.bloodgroup}</p>
            </div>
        `;
        donorListContainer.appendChild(donorInfo);
    });
}