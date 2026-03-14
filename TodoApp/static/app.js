const API = '/api/todos';
let todos = [];
let currentFilter = 'all';

// ===== API Helpers =====
async function apiFetch(url, options = {}) {
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }
  if (res.status === 204) return null;
  return res.json();
}

// ===== Load Todos =====
async function loadTodos() {
  showLoading(true);
  try {
    todos = await apiFetch(API + '/');
    render();
  } catch (err) {
    showToast('⚠️ Failed to load todos: ' + err.message);
  } finally {
    showLoading(false);
  }
}

// ===== Create Todo =====
document.getElementById('addForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const title = document.getElementById('titleInput').value.trim();
  const description = document.getElementById('descInput').value.trim();
  if (!title) return;

  const btn = document.getElementById('addBtn');
  btn.disabled = true;
  btn.textContent = 'Adding...';

  try {
    const todo = await apiFetch(API + '/', {
      method: 'POST',
      body: JSON.stringify({ title, description }),
    });
    todos.unshift(todo);
    render();
    e.target.reset();
    showToast('✅ Task added!');
  } catch (err) {
    showToast('❌ Error: ' + err.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<span class="btn-icon">+</span> Add Task';
  }
});

// ===== Toggle Complete =====
async function toggleTodo(id) {
  const todo = todos.find(t => t.id === id);
  if (!todo) return;
  try {
    const updated = await apiFetch(`${API}/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ completed: !todo.completed }),
    });
    const idx = todos.findIndex(t => t.id === id);
    todos[idx] = updated;
    render();
    showToast(updated.completed ? '✅ Marked as done!' : '🔄 Marked as active');
  } catch (err) {
    showToast('❌ Error: ' + err.message);
  }
}

// ===== Delete Todo =====
async function deleteTodo(id) {
  try {
    await apiFetch(`${API}/${id}`, { method: 'DELETE' });
    todos = todos.filter(t => t.id !== id);
    render();
    showToast('🗑️ Task deleted');
  } catch (err) {
    showToast('❌ Error: ' + err.message);
  }
}

// ===== Open Edit Modal =====
function openEdit(id) {
  const todo = todos.find(t => t.id === id);
  if (!todo) return;
  document.getElementById('editId').value = todo.id;
  document.getElementById('editTitle').value = todo.title;
  document.getElementById('editDesc').value = todo.description || '';
  document.getElementById('editModal').classList.remove('hidden');
}

function closeEdit() {
  document.getElementById('editModal').classList.add('hidden');
}

document.getElementById('cancelEdit').addEventListener('click', closeEdit);
document.getElementById('editModal').addEventListener('click', (e) => {
  if (e.target === document.getElementById('editModal')) closeEdit();
});

// ===== Save Edit =====
document.getElementById('editForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = parseInt(document.getElementById('editId').value);
  const title = document.getElementById('editTitle').value.trim();
  const description = document.getElementById('editDesc').value.trim();
  if (!title) return;

  try {
    const updated = await apiFetch(`${API}/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ title, description }),
    });
    const idx = todos.findIndex(t => t.id === id);
    todos[idx] = updated;
    render();
    closeEdit();
    showToast('✏️ Task updated!');
  } catch (err) {
    showToast('❌ Error: ' + err.message);
  }
});

// ===== Filter Tabs =====
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    currentFilter = tab.dataset.filter;
    render();
  });
});

// ===== Render =====
function render() {
  const list = document.getElementById('todoList');
  const empty = document.getElementById('emptyState');

  const filtered = todos.filter(t => {
    if (currentFilter === 'active') return !t.completed;
    if (currentFilter === 'completed') return t.completed;
    return true;
  });

  // Stats
  const total = todos.length;
  const done = todos.filter(t => t.completed).length;
  const active = total - done;
  document.getElementById('totalCount').textContent = `${total} total`;
  document.getElementById('activeCount').textContent = `${active} active`;
  document.getElementById('doneCount').textContent = `${done} done`;

  if (filtered.length === 0) {
    list.innerHTML = '';
    empty.classList.remove('hidden');
    return;
  }

  empty.classList.add('hidden');
  list.innerHTML = filtered.map(todo => `
    <div class="todo-item ${todo.completed ? 'completed' : ''}" id="todo-${todo.id}">
      <button
        class="todo-check ${todo.completed ? 'checked' : ''}"
        onclick="toggleTodo(${todo.id})"
        title="${todo.completed ? 'Mark active' : 'Mark done'}"
        aria-label="Toggle todo"
      ></button>
      <div class="todo-content">
        <div class="todo-title">${escapeHtml(todo.title)}</div>
        ${todo.description ? `<div class="todo-desc">${escapeHtml(todo.description)}</div>` : ''}
        <div class="todo-date">${formatDate(todo.created_at)}</div>
      </div>
      <div class="todo-actions">
        <button class="icon-btn edit" onclick="openEdit(${todo.id})" title="Edit" aria-label="Edit todo">✏️</button>
        <button class="icon-btn delete" onclick="deleteTodo(${todo.id})" title="Delete" aria-label="Delete todo">🗑️</button>
      </div>
    </div>
  `).join('');
}

// ===== Helpers =====
function escapeHtml(str) {
  const d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

function formatDate(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric', hour: '2-digit', minute: '2-digit' });
}

function showLoading(show) {
  document.getElementById('loadingState').classList.toggle('hidden', !show);
  document.getElementById('todoList').classList.toggle('hidden', show);
}

let toastTimer;
function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.remove('hidden');
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    toast.classList.add('hidden');
    toast.classList.remove('show');
  }, 2800);
}

// ===== Init =====
loadTodos();
