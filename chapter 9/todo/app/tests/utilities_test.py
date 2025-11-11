import unittest
from unittest.mock import AsyncMock, patch
import pytest 
from app.services import utilities
from datetime import datetime


@pytest.mark.asyncio
async def test_get_all_tasks_success():
    mock_task = [{'title' : 'test task 1', 'deadline' : '2025-11-11T19:02:31.464157'}, {'title' : 'test task 2', 'deadline' : '2025-11-11T19:02:31.464157'}]
    with patch('app.database.crud.get_all_tasks', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_task
        
        result = await utilities.get_all_tasks_or_not_found()
        
        assert result['message'] == 'ok'
        assert result['tasks'][0]['title'] == 'test task 1'
        assert result['tasks'][1]['title'] == 'test task 2'

@pytest.mark.asyncio
async def test_get_all_tasks_success():
    with patch('app.database.crud.get_all_tasks', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = None
        
        result = await utilities.get_all_tasks_or_not_found()
        
        assert result['message'] == 'no task in database.'


@pytest.mark.asyncio
async def test_get_task_by_title_found():
    mock_task = {'title' : 'test task', 'deadline' : '2025-11-11T19:02:31.464157'}
    with patch('app.database.crud.get_task_by_title', new_callable=AsyncMock) as mock:
        mock.return_value = mock_task
        
        result = await utilities.get_task_by_title_or_not_found('test task')
        
        assert result['message'] == 'ok'
        assert result['tasks']['title'] == 'test task'
        
        mock.assert_awaited_once_with('test task')


@pytest.mark.asyncio
async def test_get_task_by_title_not_found():
    with patch('app.database.crud.get_task_by_title', new_callable=AsyncMock) as mock:
        mock.return_value = None
        
        result = await utilities.get_task_by_title_or_not_found('no')
        
        assert result == {'message' : 'task not found.'}
        mock.assert_awaited_once_with('no')


@pytest.mark.asyncio
async def test_get_tasks_by_deadline_found():
    mock_task = [{'title' : 'test task 1', 'deadline' : '2025-11-11T19:02:31.464157'}, {'title' : 'test task 2', 'deadline' : '2025-11-11T19:02:31.464157'}]
    with patch('app.database.crud.get_tasks_by_deadline', new_callable=AsyncMock) as mock:
        mock.return_value = mock_task
        result = await utilities.get_tasks_by_deadline_or_not_found('2025-11-11T19:02:31.464157')
        
        assert result['message'] == 'ok'
        assert result['tasks'] == mock_task
        mock.assert_awaited_once_with(datetime.fromisoformat('2025-11-11T19:02:31.464157'))


@pytest.mark.asyncio
async def test_get_tasks_by_deadline_not_found():
    with patch('app.database.crud.get_tasks_by_deadline', new_callable=AsyncMock) as mock:
        mock.return_value = None
        
        random_time = datetime.now()
        result = await utilities.get_tasks_by_deadline_or_not_found(random_time.isoformat())
        
        assert result['message'] == 'task not found.'
        mock.assert_awaited_once_with(random_time)


@pytest.mark.asyncio
async def test_create_task_success():
    mock_task = {'title' : 'test', 'deadline' : '2025-11-11T19:02:31.464157'}
    with patch('app.database.crud.create_task', new_callable=AsyncMock) as mock_create, patch('app.services.utilities.get_task_by_title_or_not_found', new_callable=AsyncMock) as mock_get:
        mock_create.return_value = True
        mock_get.return_value = mock_task
        
        result = await utilities.create_task_or_fail('test', '2025-11-11T19:02:31.464157')
        
        assert result['message'] == 'ok'
        assert result['tasks']['title'] == 'test'
        assert result['tasks']['deadline'] == '2025-11-11T19:02:31.464157'
        
        mock_create.assert_awaited_once_with('test', datetime.fromisoformat('2025-11-11T19:02:31.464157'))
        mock_get.assert_awaited_once_with('test')


@pytest.mark.asyncio
async def test_create_task_fail():
    with patch('app.database.crud.create_task', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = False
        
        result = await utilities.create_task_or_fail('test', '2025-11-11T19:02:31.464157')
        assert result['message'] == 'task has not been created'
        
        mock_create.assert_awaited_once_with('test', datetime.fromisoformat('2025-11-11T19:02:31.464157'))


@pytest.mark.asyncio
async def test_delete_task_success():
    mock_task = {'title' : 'test 1', 'deadline' : '2025-11-11T19:02:31.464157'}
    
    with patch('app.database.crud.delete_task', new_callable=AsyncMock) as mock_delete, patch('app.database.crud.get_task_by_title', new_callable=AsyncMock) as mock_get:
        mock_delete.return_value = True
        mock_get.return_value = mock_task

        result = await utilities.delete_task_or_fail('test 1')
        
        assert result['message'] == 'task deleted'


@pytest.mark.asyncio
async def test_delete_task_fail():
    mock_task = {'title' : 'test 1', 'deadline' : '2025-11-11T19:02:31.464157'}
    
    with patch('app.database.crud.delete_task', new_callable=AsyncMock) as mock_delete, patch('app.database.crud.get_task_by_title', new_callable=AsyncMock) as mock_get:
        mock_delete.return_value = False
        mock_get.return_value = mock_task

        result = await utilities.delete_task_or_fail('test 1')
        
        assert result['message'] == 'task did not delete'
