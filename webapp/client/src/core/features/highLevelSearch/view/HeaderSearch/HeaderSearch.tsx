import { InputAdornment } from '@material-ui/core';
import * as React from 'react';
import { connect } from 'react-redux';
import { useHistory, useParams } from 'react-router';
import * as R from 'ramda';

import { Icon } from 'core/shared/view/elements/Icon/Icon';
import MuiTextInput from 'core/shared/view/elements/MuiTextInput/MuiTextInput';
import routes, { GetRouteParams } from 'routes';
import { IApplicationState } from 'store/store';
import { selectCurrentWorkspaceName } from 'store/workspaces';

import styles from './HeaderSearch.module.css';
import { defaultFilter } from '../../constants';
import { defaultResultsSorting } from 'core/shared/models/HighLevelSearch';

const mapStateToProps = (state: IApplicationState) => ({
  currentWorkspaceName: selectCurrentWorkspaceName(state),
});

type AllProps = ReturnType<typeof mapStateToProps>;

const HeaderSearch = ({ currentWorkspaceName }: AllProps) => {
  const [value, changeValue] = React.useState<string>('');
  const history = useHistory();

  const currentQueryParams = routes.highLevelSearch.parseQueryParams(history.location.search) || {};
  const queryParams = { ...currentQueryParams, q: value, type: currentQueryParams.type || defaultFilter };

  const redirectToHighLevelSearchWithValue = () => {
    history.push(
      routes.highLevelSearch.getRedirectPathWithQueryParams({
        params: { workspaceName: currentWorkspaceName },
        queryParams,
      })
    );
  };

  return (
    <div className={styles.root}>
      <MuiTextInput
        value={value}
        placeholder="Search"
        classes={{
          root: styles.root,
        }}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <Icon
                type="search"
                className={styles.icon}
                onClick={redirectToHighLevelSearchWithValue}
              />
            </InputAdornment>
          ),
        }}
        onKeyUp={e => {
          // when press enter
          if (e.keyCode === 13) {
            redirectToHighLevelSearchWithValue();
          }
        }}
        onChange={e => changeValue(e.currentTarget.value)}
      />
    </div>
  );
};

export default connect(mapStateToProps)(HeaderSearch);
