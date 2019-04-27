# Testing

Writing tests, rules, managing them with loads of examples

## Table of contents

- [Concepts](#concepts)
- [TDD Rules](#tdd-rules)
- [Magic Tricks of Testing](#magic-tricks-of-testing)
  - [Message Testing Rules](#message-testing-rules)

### Concepts

#### Types of Test

- **Unit tests**: Make sure a class or a function works as expected in isolation
- **Functional tests**: Verify that the microservice does what it says from the consumer's point of view, and behaves correctly even on bad requests
- **Integration tests**: Verify how a microservice integrates with all its network dependencies
- **Load tests**: Measure the microservice performances
- **End-to-end tests**: Verify that the whole system works with an end-to-end test

### TDD Rules

- Write Tests First, Code Letter
- Add the reasonably amount of code you need to pass the tests
- You Shouldn't have more than one failing test
- Write code that passes the test and refactor it
- A test should fail the first time you run it. If it doesn’t, ask yourself why you are adding it.
- Never refactor w/o tests.

#### How many assertions

- If the test conditions are logical `AND` - then go for multiple assertions.
- if the conditions are logical - `OR` - Multiple Test functions.

#### How to Fix Bugs

From the TDD point of view, if you don’t have a failing test there is no bug, so you have to come up with at least one test that exposes the issue you are trying to solve.

### Magic Tricks of Testing

Testing should be based on the message flow between objects. For Example there are two types of messages -

1. **Query** - Return Something / Change Nothing
2. **Command** - Return Nothing / Change

And There are three ways message can flow between objects

1. **Incoming Messages** - messages a method receives
2. **Self to Self Messages** - calling to private method
3. **Outgoing Messages** - messages a method return to another method

![message-flow](./images/message-flow.jpg)

#### Message Testing Rules

- **Incoming Query Message** - test incoming query messages by making assertions about what they send back. Also test the interface not the implementation.

  Now this following method should return the 2\*input. For example if you give 2 it should return 4. It's a query message because whatever you send it does not change the state, rather it does some computation and return the value.

  ```py
  class Hello:
      def world(self, x):
          return x*2
  ```

  To test it we should only need to assert the return value. We don't what it does inside from a TDD point of view.

  ```py
  def test_world():
      assert Hello().world(2) == 4
  ```

- **Incoming Command Message** - Assert about direct public side effects. For example - we might call a setter to set a value. By this way we are directly changing it's state. So we need to assert the changed state

  ```py
  class Hello:
      def set_world(self, x):
          self.world_name = x
  ```

  ```py
  def test_set_world():
      h = Hello()
      h.set_world('earth')
      assert h.world_name == 'earth'
  ```

- **Self-to-self Query/Command Message** - These are the conditions when a public method calls a private method. The Whole Application does not know about it. Only the public method are supposed to access it.

  If the tested public method can access it and got the expected value it should, then no need to test it.

- **Outgoing Query Message** - Say for example we are passing a value to another method. If it does not change the state we should not test it. Cause we are already testing `Incoming Query Message`.
- **Outgoing Command Message** - they directly change the state of others by calling setters. There is a clear distinction between `Incoming Command` and `Outgoing Command`. For Example if we are testing the `setter` method than we call it `Incoming Command`, otherwise `Outgoing Commnad`. Use a `Mock Object` to hide the implementation. Cause this is a `unit test` not the `integration test`.

  **Mock Objects and their originals** should play by **common API**.

![rules-of-testing-for-different-types-of-messages](./images/test-table-with-messages.png)

## Built With

- [pytest](https://docs.pytest.org/en/latest/) - The testing framework used for python

## Contributing

Please read [CONTRIBUTING.md](./.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Alamin Mahamud** - _Initial work_ - [alamin-mahamud](https://github.com/alamin-mahamud)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

## Resources

- [The magic tricks of testing](https://speakerdeck.com/skmetz/magic-tricks-of-testing-railsconf)
