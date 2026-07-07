let livresVisibles = true;
let utilisateursVisibles = true;
let empruntsVisibles = true;

/* =========================
   DASHBOARD
========================= */

async function chargerDashboard() {
    try {
        const livres = await (await fetch("http://localhost:8000/books")).json();
        const users = await (await fetch("http://localhost:8001/users")).json();
        const emprunts = await (await fetch("http://localhost:8002/history")).json();
        
        let totalRetards = 0;

        emprunts.forEach(emprunt => {

            const dateEmprunt =
                new Date(emprunt.date_emprunt);

            const dateLimite =
                new Date(dateEmprunt);

            dateLimite.setDate(
                dateLimite.getDate() + 15
            );

            if (
                !emprunt.retourne &&
                new Date() > dateLimite
            ) {
                totalRetards++;
            }
        });

        document.getElementById("totalLivres").innerText = livres.length;
        document.getElementById("totalUtilisateurs").innerText = users.length;
        document.getElementById("totalEmprunts").innerText = emprunts.length;
        document.getElementById("totalRetards").innerText = totalRetards;

    } catch (error) {
        console.error("Erreur chargement dashboard :", error);
    }
}

/* =========================
   LIVRES
========================= */

async function chargerLivres() {
    const livres = await (await fetch("http://localhost:8000/books")).json();
    afficherLivres(livres);
}

function afficherLivres(livres) {
    const container = document.getElementById("livres");

    if (livres.length === 0) {
        container.innerHTML = "<p>Aucun livre trouvé.</p>";
        return;
    }

    let table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Titre</th>
                    <th>Auteur</th>
                    <th>ISBN</th>
                    <th>Année</th>
                    <th>Disponibilité</th>
                </tr>
            </thead>
            <tbody>
    `;

    livres.forEach(livre => {
        table += `
            <tr>
                <td>${livre.id}</td>
                <td>${livre.title}</td>
                <td>${livre.author}</td>
                <td>${livre.isbn}</td>
                <td>${livre.publication_year}</td>
                <td>${livre.available ? "🟢 Disponible" : "🔴 Indisponible"}</td>
            </tr>
        `;
    });

    table += `
            </tbody>
        </table>
    `;

    container.innerHTML = table;
}

/* =========================
   RECHERCHE
========================= */

async function rechercherLivre() {
    const valeur = document.getElementById("searchValue").value.trim();
    const critere = document.getElementById("searchType").value;

    if (valeur === "") {
        chargerLivres();
        return;
    }

    const livres = await (
        await fetch(`http://localhost:8000/books/search?${critere}=${encodeURIComponent(valeur)}`)
    ).json();

    afficherLivres(livres);
}

function effacerRecherche() {
    document.getElementById("searchValue").value = "";
    document.getElementById("searchType").value = "title";
    chargerLivres();
}

/* =========================
   UTILISATEURS
========================= */

async function chargerUtilisateurs() {
    const utilisateurs = await (await fetch("http://localhost:8001/users")).json();
    const container = document.getElementById("utilisateurs");

    let table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nom</th>
                    <th>Email</th>
                    <th>Type</th>
                    <th>Actif</th>
                </tr>
            </thead>
            <tbody>
    `;

    utilisateurs.forEach(user => {
        table += `
            <tr>
                <td>${user.id}</td>
                <td>${user.nom}</td>
                <td>${user.email}</td>
                <td>${user.type_utilisateur}</td>
                <td>${user.actif ? "🟢 Oui" : "🔴 Non"}</td>
            </tr>
        `;
    });

    table += `
            </tbody>
        </table>
    `;

    container.innerHTML = table;
}

/* =========================
   EMPRUNTS
========================= */

async function chargerEmprunts() {
    const users = await (await fetch("http://localhost:8001/users")).json();
    const books = await (await fetch("http://localhost:8000/books")).json();
    const borrows = await (await fetch("http://localhost:8002/history")).json();

    const container = document.getElementById("emprunts");

    let table = `
        <table>
            <thead>
                <tr>
                    <th>Utilisateur</th>
                    <th>Type</th>
                    <th>Livre</th>
                    <th>Auteur</th>
                    <th>Date emprunt</th>
                    <th>Date limite</th>
                    <th>Jours restants</th>
                    <th>Retard</th>
                    <th>Date retour</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
    `;

    borrows.forEach(borrow => {
        const user = users.find(u => u.id === borrow.user_id);
        const book = books.find(b => b.id === borrow.book_id);

        const dateEmprunt = new Date(borrow.date_emprunt);
        const dateLimite = new Date(dateEmprunt);
        dateLimite.setDate(dateLimite.getDate() + 15);

        const aujourdHui = new Date();
        const joursRestants = Math.ceil((dateLimite - aujourdHui) / (1000 * 60 * 60 * 24));

        let restant = "-";
        let retard = "-";
        let statut = "🟢 En cours";
        let cssClass = "status-ok";

        if (borrow.retourne) {
            statut = "🔵 Retourné";
            cssClass = "status-returned";
        } else {
            if (joursRestants >= 0) {
                restant = `🟢 ${joursRestants} jour(s)`;
            } else {
                retard = `🔴 ${Math.abs(joursRestants)} jour(s)`;
                statut = "🔴 En retard";
                cssClass = "status-late";
            }
        }

        table += `
            <tr>
                <td>${user ? user.nom : "Utilisateur inconnu"}</td>
                <td>${user ? user.type_utilisateur : "-"}</td>
                <td>${book ? book.title : "Livre inconnu"}</td>
                <td>${book ? book.author : "-"}</td>
                <td>${formatDate(borrow.date_emprunt)}</td>
                <td>${dateLimite.toLocaleDateString("fr-FR")}</td>
                <td>${restant}</td>
                <td class="status-late">${retard}</td>
                <td>${borrow.date_retour ? formatDate(borrow.date_retour) : "-"}</td>
                <td class="${cssClass}">${statut}</td>
            </tr>
        `;
    });

    table += `
            </tbody>
        </table>
    `;

    container.innerHTML = table;
}

/* =========================
   DATE
========================= */

function formatDate(dateString) {
    if (!dateString) return "-";
    return new Date(dateString).toLocaleDateString("fr-FR");
}

/* =========================
   ACTUALISATION
========================= */

async function actualiserDonnees() {
    await chargerDashboard();

    if (livresVisibles) await chargerLivres();
    if (utilisateursVisibles) await chargerUtilisateurs();
    if (empruntsVisibles) await chargerEmprunts();
}

/* =========================
   TOGGLE
========================= */

async function toggleLivres() {
    const contenu = document.getElementById("livres");
    const bouton = document.getElementById("btnLivres");

    if (livresVisibles) {
        contenu.innerHTML = "";
        bouton.innerText = "Afficher les livres";
    } else {
        await chargerLivres();
        bouton.innerText = "Masquer les livres";
    }

    livresVisibles = !livresVisibles;
}

async function toggleUtilisateurs() {
    const contenu = document.getElementById("utilisateurs");
    const bouton = document.getElementById("btnUtilisateurs");

    if (utilisateursVisibles) {
        contenu.innerHTML = "";
        bouton.innerText = "Afficher les utilisateurs";
    } else {
        await chargerUtilisateurs();
        bouton.innerText = "Masquer les utilisateurs";
    }

    utilisateursVisibles = !utilisateursVisibles;
}

async function toggleEmprunts() {
    const contenu = document.getElementById("emprunts");
    const bouton = document.getElementById("btnEmprunts");

    if (empruntsVisibles) {
        contenu.innerHTML = "";
        bouton.innerText = "Afficher les emprunts";
    } else {
        await chargerEmprunts();
        bouton.innerText = "Masquer les emprunts";
    }

    empruntsVisibles = !empruntsVisibles;
}

/* =========================
   DEMARRAGE
========================= */

window.onload = async function () {
    await chargerDashboard();
    await chargerLivres();
    await chargerUtilisateurs();
    await chargerEmprunts();

    document.getElementById("btnLivres").innerText = "Masquer les livres";
    document.getElementById("btnUtilisateurs").innerText = "Masquer les utilisateurs";
    document.getElementById("btnEmprunts").innerText = "Masquer les emprunts";
};