name: Task Issue
description: Use this template to create task issues.

title: "[Task] - "
body:
  - type: markdown
    attributes:
      value: "## Task Issue"
  - type: input
    id: task_summary
    attributes:
      label: Summary
      description: "A brief summary of the task."
      placeholder: "Describe the task here"
      required: true
  - type: textarea
    id: details
    attributes:
      label: Details
      description: "Provide additional details about the task."
      placeholder: "Describe the task in detail"
  - type: markdown
    attributes:
      value: "## Subtasks"
  - type: textarea
    id: subtasks
    attributes:
      label: Subtasks
      description: "List any subtasks that need to be completed."
      placeholder: "List subtasks here"
