document.getElementById("question").addEventListener("input", function() {
	console.log(this.scrollHeight);
    this.style.height = "auto";
    this.style.height = (this.scrollHeight - 40) + "px";
});

function getTagSuggestions() {
    const question = document.getElementById('question').value;
    fetch('http://localhost/flask/api/v1/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        const tagSuggestions = document.getElementById('tag-suggestions');
        tagSuggestions.innerHTML = '';

        data.forEach(tag => {
            const tagElement = document.createElement('div');
            tagElement.classList.add('tag');
            tagElement.textContent = tag.tag;
            tagElement.onclick = () => selectTag(tagElement);
            tagSuggestions.appendChild(tagElement);
        });
    })
    .catch(error => console.error('Erreur:', error));
}

function selectTag(tagElement) {
    const selectedTagsContainer = document.getElementById('selected-tags');
    const tagClone = tagElement.cloneNode(true);
    tagClone.classList.add('selected');
    selectedTagsContainer.appendChild(tagClone);

    tagElement.style.display = 'none';
}

function validateTags() {
    const selectedTags = [];
    document.querySelectorAll('#selected-tags .tag').forEach(tag => {
        selectedTags.push(tag.textContent);
    });

    fetch('http://localhost/flask/api/v1/validate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tags: selectedTags })
    })
    .then(response => response.json())
    .then(data => {
		console.log(data);
		const selectedTagsContainer = document.getElementById('selected-tags');
        selectedTagsContainer.innerHTML = '';
		const tagSuggestions = document.getElementById('tag-suggestions');
		tagSuggestions.innerHTML = '';
		return data;
    })
	.then(data => {
		alert('Tags validés avec succès ' + data.tags);
	})
    .catch(error => console.error('Erreur:', error));
}
