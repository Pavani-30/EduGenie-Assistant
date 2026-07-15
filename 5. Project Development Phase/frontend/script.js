const moduleBtns = document.querySelectorAll('.module-btn');
const panels = document.querySelectorAll('.panel');
const results = document.getElementById('results');

moduleBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    moduleBtns.forEach((b) => b.classList.remove('active'));
    panels.forEach((p) => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(`panel-${btn.dataset.module}`).classList.add('active');
    results.innerHTML = '<div class="results-empty">Your results will appear here.</div>';
  });
});

panels.forEach((form) => {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const endpoint = form.dataset.endpoint;
    const button = form.querySelector('button');
    const originalLabel = button.dataset.label || button.textContent;
    button.dataset.label = originalLabel;
    const data = Object.fromEntries(new FormData(form).entries());

    if (data.num_questions) data.num_questions = Number(data.num_questions);

    button.disabled = true;
    button.textContent = 'Thinking...';
    results.textContent = 'EduGenie is working on it...';

    try {
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const payload = await res.json();
      if (!res.ok) throw new Error(payload.detail || 'Something went wrong.');
      results.textContent = payload.result;
    } catch (err) {
      results.innerHTML = `<span class="error">Error: ${err.message}</span>`;
    } finally {
      button.disabled = false;
      button.textContent = originalLabel;
    }
  });
});
