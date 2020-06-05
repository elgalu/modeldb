import { connectRouter, RouterState } from 'connected-react-router';
import { History } from 'history';
import { Action, AnyAction, combineReducers, Dispatch } from 'redux';
import { ThunkAction } from 'redux-thunk';
import { ApolloClient } from 'apollo-boost';

import ServiceFactory from 'services/ServiceFactory';

import * as HighLevelSearch from 'core/features/highLevelSearch';
import * as CompareEntities from 'core/features/compareEntities';
import * as RepositoryNavigation from 'core/features/versioning/repositoryNavigation';
import * as ExperimentRunsTableConfig from 'core/features/experimentRunsTableConfig';
import * as Filter from 'core/features/filter';
import * as Layout from 'core/features/Layout';
import * as Comment from 'features/comments';
import * as Workspaces from 'features/workspaces/store';

import {
  IArtifactManagerState,
  artifactManagerReducer,
} from './artifactManager';
import { IDatasetsState, datasetsReducer } from './datasets';
import {
  IDatasetVersionsState,
  datasetVersionsReducer,
} from './datasetVersions';
import {
  IDescriptionActionState,
  descriptionActionReducer,
} from './descriptionAction';
import { experimentRunsReducer, IExperimentRunsState } from './experimentRuns';
import { IExperimentsState, experimentsReducer } from './experiments';
import {
  IProjectCreationState,
  projectCreationReducer,
} from './projectCreation';
import { IProjectsState, projectsReducer } from './projects';
import { IProjectsPageState, projectsPageReducer } from './projectsPage';
import { ITagActionState, tagActionReducer } from './tagAction';

export interface IApplicationState
  extends Filter.IFilterRootState,
    Comment.ICommentsRootState,
    ExperimentRunsTableConfig.IExperimentRunsTableConfigRootState,
    Layout.ILayoutRootState {
  experiments: IExperimentsState;
  compareEntities: CompareEntities.ICompareEntitiesState;
  experimentRuns: IExperimentRunsState;
  projectCreation: IProjectCreationState;
  projects: IProjectsState;
  projectsPage: IProjectsPageState;
  router: RouterState;
  tagAction: ITagActionState;
  descriptionAction: IDescriptionActionState;
  artifactManager: IArtifactManagerState;
  datasets: IDatasetsState;
  datasetVersions: IDatasetVersionsState;
  workspaces: Workspaces.IWorkspaces;
  repositoryNavigation: RepositoryNavigation.types.IRepositoryNavigationState;
  highLevelSearch: HighLevelSearch.types.IHighLevelSearchState;
}

// Additional props for connected React components. This prop is passed by default with `connect()`
export interface IConnectedReduxProps<A extends Action = any> {
  dispatch: Dispatch<A>;
}

export const createRootReducer = (history: History) =>
  combineReducers<IApplicationState>({
    layout: Layout.layoutReducer,
    experiments: experimentsReducer,
    comments: Comment.commentsReducer,
    compareEntities: CompareEntities.compareModelsReducer,
    experimentRunsTableConfig:
      ExperimentRunsTableConfig.experimentRunsTableConfigReducer,
    experimentRuns: experimentRunsReducer,
    filters: Filter.filtersReducer,
    projectCreation: projectCreationReducer,
    projects: projectsReducer,
    projectsPage: projectsPageReducer,
    router: connectRouter(history),
    tagAction: tagActionReducer,
    descriptionAction: descriptionActionReducer,
    artifactManager: artifactManagerReducer,
    datasets: datasetsReducer,
    datasetVersions: datasetVersionsReducer,
    workspaces: Workspaces.workspacesReducer,
    repositoryNavigation: RepositoryNavigation.reducer,
    highLevelSearch: HighLevelSearch.reducer,
  });

export interface IThunkActionDependencies
  extends Filter.IThunkActionDependencies,
    Comment.IThunkActionDependencies<
      IApplicationState,
      Comment.Model.IComment
    > {
  ServiceFactory: typeof ServiceFactory;
  history: History;
  apolloClient: ApolloClient<any>;
}

export type ActionResult<R = void, A extends Action = AnyAction> = ThunkAction<
  R,
  IApplicationState,
  IThunkActionDependencies,
  A
>;
