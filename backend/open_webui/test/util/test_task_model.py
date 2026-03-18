# [PT-F5F7] Let models override the task model used for background tasks.
from open_webui.utils.task import get_task_model_id


def build_model(
    connection_type: str = "local",
    task_model_id: str | None = None,
    base_model_id: str | None = None,
):
    meta = {}
    if task_model_id is not None:
        meta["__task_model_id__"] = task_model_id

    info = {"meta": meta}
    if base_model_id is not None:
        info["base_model_id"] = base_model_id

    return {"connection_type": connection_type, "info": info}


class TestGetTaskModelId:
    def test_model_override_wins_global_task_model(self):
        models = {
            "chat-model": build_model(task_model_id="override-model"),
            "override-model": build_model(),
            "global-task-model": build_model(),
        }

        result = get_task_model_id(
            "chat-model", "global-task-model", "global-task-model", models
        )

        assert result == "override-model"

    def test_empty_override_falls_back_to_local_global_task_model(self):
        models = {
            "chat-model": build_model(task_model_id=""),
            "global-task-model": build_model(),
        }

        result = get_task_model_id("chat-model", "global-task-model", "", models)

        assert result == "global-task-model"

    def test_invalid_override_falls_back_to_external_global_task_model(self):
        models = {
            "chat-model": build_model(
                connection_type="external", task_model_id="missing-model"
            ),
            "global-external-task-model": build_model(connection_type="external"),
        }

        result = get_task_model_id(
            "chat-model", "", "global-external-task-model", models
        )

        assert result == "global-external-task-model"

    def test_models_without_override_keep_existing_behavior(self):
        models = {
            "chat-model": build_model(),
        }

        result = get_task_model_id("chat-model", "", "", models)

        assert result == "chat-model"

    def test_custom_model_does_not_inherit_override_from_base_model(self):
        models = {
            "custom-model": build_model(base_model_id="base-model"),
            "base-model": build_model(task_model_id="base-task-model"),
            "global-task-model": build_model(),
        }

        result = get_task_model_id("custom-model", "global-task-model", "", models)

        assert result == "global-task-model"
